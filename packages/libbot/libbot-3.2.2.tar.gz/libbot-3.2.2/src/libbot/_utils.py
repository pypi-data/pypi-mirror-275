import inspect
from typing import Callable


def supports_argument(func: Callable, arg_name: str) -> bool:
    """Check whether a function has a specific argument

    ### Args:
        * func (`Callable`): Function to be inspected
        * arg_name (`str`): Argument to be checked

    ### Returns:
        * `bool`: `True` if argument is supported and `False` if not
    """
    if hasattr(func, "__code__"):
        return arg_name in inspect.signature(func).parameters
    elif hasattr(func, "__doc__"):
        if doc := func.__doc__:
            first_line = doc.splitlines()[0]
            return arg_name in first_line

    return False
