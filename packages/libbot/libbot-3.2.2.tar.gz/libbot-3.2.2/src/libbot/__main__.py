from pathlib import Path
from typing import Any, Union

import aiofiles

try:
    from ujson import dumps, loads
except ImportError:
    from json import dumps, loads

from ._utils import supports_argument
from .sync._nested import nested_delete, nested_set


async def json_read(path: Union[str, Path]) -> Any:
    """Read contents of a JSON file

    ### Args:
        * path (`Union[str, Path]`): Path-like object or path as a string

    ### Returns:
        * `Any`: File contents
    """
    async with aiofiles.open(str(path), mode="r", encoding="utf-8") as f:
        data = await f.read()

    return loads(data)


async def json_write(data: Any, path: Union[str, Path]) -> None:
    """Write contents to a JSON file

    ### Args:
        * data (`Any`): Contents to write. Must be a JSON serializable
        * path (`Union[str, Path]`): Path-like object or path as a string of a destination
    """
    async with aiofiles.open(str(path), mode="w", encoding="utf-8") as f:
        await f.write(
            dumps(data, ensure_ascii=False, escape_forward_slashes=False, indent=4)
            if supports_argument(dumps, "escape_forward_slashes")
            else dumps(data, ensure_ascii=False, indent=4)
        )


async def config_get(
    key: str, *path: str, config_file: Union[str, Path] = "config.json"
) -> Any:
    """Get a value of the config key by its path provided
    For example, `foo.bar.key` has a path of `"foo", "bar"` and the key `"key"`

    ### Args:
        * key (`str`): Key that contains the value
        * *path (`str`): Path to the key that contains the value
        * config_file (`Union[str, Path]`, *optional*): Path-like object or path as a string of a location of the config file. Defaults to `"config.json"`

    ### Returns:
        * `Any`: Key's value

    ### Example:
    Get the "salary" of "Pete" from this JSON structure:
    ```json
    {
        "users": {
            "Pete": {
                "salary": 10.0
            }
        }
    }
    ```

    This can be easily done with the following code:
    ```python
    import libbot
    salary = await libbot.config_get("salary", "users", "Pete")
    ```
    """
    this_key = await json_read(config_file)

    for dict_key in path:
        this_key = this_key[dict_key]

    return this_key[key]


async def config_set(
    key: str, value: Any, *path: str, config_file: Union[str, Path] = "config.json"
) -> None:
    """Set config's key by its path to the value

    ### Args:
        * key (`str`): Key that leads to the value
        * value (`Any`): Any JSON serializable data
        * *path (`str`): Path to the key of the target
        * config_file (`Union[str, Path]`, *optional*): Path-like object or path as a string of a location of the config file. Defaults to `"config.json"`

    ### Raises:
        * `KeyError`: Key is not found under path provided
    """
    await json_write(
        nested_set(await json_read(config_file), value, *(*path, key)), config_file
    )
    return


async def config_delete(
    key: str,
    *path: str,
    missing_ok: bool = False,
    config_file: Union[str, Path] = "config.json",
) -> None:
    """Set config's key by its path

    ### Args:
        * key (`str`): Key to delete
        * *path (`str`): Path to the key of the target
        * missing_ok (`bool`): Do not raise an exception if the key is missing. Defaults to `False`
        * config_file (`Union[str, Path]`, *optional*): Path-like object or path as a string of a location of the config file. Defaults to `"config.json"`

    ### Raises:
        * `KeyError`: Key is not found under path provided and `missing_ok` is `False`
    """
    config_data = await json_read(config_file)

    try:
        nested_delete(config_data, *(*path, key))
    except KeyError as exc:
        if not missing_ok:
            raise exc from exc

    await json_write(config_data, config_file)
