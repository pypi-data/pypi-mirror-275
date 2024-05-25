from functools import wraps
import concurrent.futures
from typing import Callable, Any, Dict, List
from swarms.tools.py_func_to_openai_func_str import (
    get_openai_function_schema_from_func,
)
from swarms.utils.loguru_logger import logger


def tool(
    name: str = None,
    description: str = None,
    return_dict: bool = True,
    verbose: bool = True,
    return_string: bool = False,
    return_yaml: bool = False,
):
    """
    A decorator function that generates an OpenAI function schema.

    Args:
        name (str, optional): The name of the OpenAI function. Defaults to None.
        description (str, optional): The description of the OpenAI function. Defaults to None.
        *args: Variable length argument list.
        **kwargs: Arbitrary keyword arguments.

    Returns:
        dict: The generated OpenAI function schema.

    """

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                # Log the function call
                logger.info(f"Creating Tool: {func.__name__}")

                # Assert that the arguments are of the correct type
                assert isinstance(name, str), "name must be a string"
                assert isinstance(
                    description, str
                ), "description must be a string"
                assert isinstance(
                    return_dict, bool
                ), "return_dict must be a boolean"
                assert isinstance(
                    verbose, bool
                ), "verbose must be a boolean"

                # Call the function
                func(*args, **kwargs)

                # Get the openai function schema
                tool_name = name if not None else func.__name__
                schema = get_openai_function_schema_from_func(
                    func, name=tool_name, description=description
                )

                # Return the schema
                if return_dict:
                    return schema
                elif return_string is True:
                    return str(schema)
                elif return_yaml is True:
                    # schema = YamlModel().dict_to_yaml(schema)
                    return schema
                else:
                    return schema

            except AssertionError as e:
                # Log the assertion error
                logger.error(f"Assertion error: {str(e)}")
                raise

            except Exception as e:
                # Log the exception
                logger.error(f"Exception occurred: {str(e)}")
                raise

        return wrapper

    return decorator


def openai_tool_executor(
    tools: List[Dict[str, Any]],
    function_map: Dict[str, Callable],
    verbose: bool = True,
    return_as_string: bool = False,
    *args,
    **kwargs,
) -> Callable:
    """
    Creates a function that dynamically and concurrently executes multiple functions based on parameters specified
    in a list of tool dictionaries, with extensive error handling and validation.

    Args:
        tools (List[Dict[str, Any]]): A list of dictionaries, each containing configuration for a tool, including parameters.
        function_map (Dict[str, Callable]): A dictionary mapping function names to their corresponding callable functions.
        verbose (bool): If True, enables verbose logging.
        return_as_string (bool): If True, returns the results as a concatenated string.

    Returns:
        Callable: A function that, when called, executes the specified functions concurrently with the parameters given.

    Examples:
    >>> def test_function(param1: int, param2: str) -> str:
    ...     return f"Test function called with parameters: {param1}, {param2}"

    >>> tool_executor = openai_tool_executor(
    ...     tools=[
    ...         {
    ...             "type": "function",
    ...             "function": {
    ...                 "name": "test_function",
    ...                 "parameters": {
    ...                     "param1": 1,
    ...                     "param2": "example"
    ...                 }
    ...             }
    ...         }
    ...     ],
    ...     function_map={
    ...         "test_function": test_function
    ...     },
    ...     return_as_string=True
    ... )
    >>> results = tool_executor()
    >>> print(results)
    """

    def tool_executor():
        # Prepare tasks for concurrent execution
        results = []
        logger.info(f"Executing {len(tools)} tools concurrently.")
        with concurrent.futures.ThreadPoolExecutor() as executor:
            futures = []
            for tool in tools:
                if tool.get("type") != "function":
                    continue  # Skip non-function tool entries

                function_info = tool.get("function", {})
                func_name = function_info.get("name")
                logger.info(f"Executing function: {func_name}")

                # Check if the function name is mapped to an actual function
                if func_name not in function_map:
                    error_message = f"Function '{func_name}' not found in function map."
                    logger.error(error_message)
                    results.append(error_message)
                    continue

                # Validate parameters
                params = function_info.get("parameters", {})
                if not params:
                    error_message = f"No parameters specified for function '{func_name}'."
                    logger.error(error_message)
                    results.append(error_message)
                    continue

                # Submit the function for execution
                try:
                    future = executor.submit(
                        function_map[func_name], **params
                    )
                    futures.append((func_name, future))
                except Exception as e:
                    error_message = f"Failed to submit the function '{func_name}' for execution: {e}"
                    logger.error(error_message)
                    results.append(error_message)

            # Gather results from all futures
            for func_name, future in futures:
                try:
                    result = future.result()  # Collect result from future
                    results.append(f"{func_name}: {result}")
                except Exception as e:
                    error_message = f"Error during execution of function '{func_name}': {e}"
                    logger.error(error_message)
                    results.append(error_message)

        if return_as_string:
            return "\n".join(results)

        logger.info(f"Results: {results}")

        return results

    return tool_executor


# # Example
# @tool(
#     name="test_function",
#     description="A test function that takes two parameters and returns a string.",
# )
# def test_function(param1: int, param2: str) -> str:
#     return f"Test function called with parameters: {param1}, {param2}"


# @tool(
#     name="test_function2",
#     description="A test function that takes two parameters and returns a string.",
# )
# def test_function2(param1: int, param2: str) -> str:
#     return f"Test function 2 called with parameters: {param1}, {param2}"


# # Example execution
# out = openai_tool_executor(
#     tools=[
#         {
#             "type": "function",
#             "function": {
#                 "name": "test_function",
#                 "parameters": {
#                     "properties": {
#                         "param1": {
#                             "type": "int",
#                             "description": "An integer parameter.",
#                         },
#                         "param2": {
#                             "type": "str",
#                             "description": "A string parameter.",
#                         },
#                     }
#                 },
#             },
#         },
#         {
#             "type": "function",
#             "function": {
#                 "name": "test_function2",
#                 "parameters": {
#                     "properties": {
#                         "param1": {
#                             "type": "int",
#                             "description": "An integer parameter.",
#                         },
#                         "param2": {
#                             "type": "str",
#                             "description": "A string parameter.",
#                         },
#                     }
#                 },
#             },
#         },
#     ],
#     function_map={
#         "test_function": test_function,
#         "test_function2": test_function2,
#     },
#     return_as_string=True,
# )
# print(out)
