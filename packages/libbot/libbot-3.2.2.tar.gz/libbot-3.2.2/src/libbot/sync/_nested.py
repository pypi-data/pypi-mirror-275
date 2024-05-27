from typing import Any, Dict


def nested_set(
    target: dict, value: Any, *path: str, create_missing=True
) -> Dict[str, Any]:
    """Set the key by its path to the value

    ### Args:
        * target (`dict`): Dictionary to perform modifications on
        * value (`Any`): Any data
        * *path (`str`): Path to the key of the target
        * create_missing (`bool`, *optional*): Create keys on the way if they're missing. Defaults to `True`

    ### Raises:
        * `KeyError`: Key is not found under path provided

    ### Returns:
        * `Dict[str, Any]`: Changed dictionary
    """
    d = target

    for key in path[:-1]:
        if key in d:
            d = d[key]
        elif create_missing:
            d = d.setdefault(key, {})
        else:
            raise KeyError(
                f"Key '{key}' is not found under path provided ({path}) and create_missing is False"
            )

    if path[-1] in d or create_missing:
        d[path[-1]] = value

    return target


def nested_delete(target: dict, *path: str) -> Dict[str, Any]:
    """Delete the key by its path

    ### Args:
        * target (`dict`): Dictionary to perform modifications on

    ### Raises:
        * `KeyError`: Key is not found under path provided

    ### Returns:
        `Dict[str, Any]`: Changed dictionary
    """
    d = target

    for key in path[:-1]:
        if key in d:
            d = d[key]
        else:
            raise KeyError(f"Key '{key}' is not found under path provided ({path})")

    if path[-1] in d:
        del d[path[-1]]
    else:
        raise KeyError(f"Key '{path[-1]}' is not found under path provided ({path})")

    return target
