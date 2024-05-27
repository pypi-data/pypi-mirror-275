import json
from pathlib import Path
from typing import Any, Union, Optional


def json_dump(filepath: Union[str, Path], data: Any, indent: Optional[int] = None) -> Union[str, Path]:
    """
    Write JSON serializable data to a file.

    Args:
        filepath (Union[str, Path]): The file path where the JSON data will be written.
        data (Any): The JSON serializable data to be written to the file.
        indent (Optional[int]): If specified, the number of spaces used for indentation.

    Returns:
        Union[str, Path]: The file path where the JSON data was written.

    Raises:
        TypeError: If `filepath` is not a string or a Path object.

    Example:
        j_dumps("data.json", {"key": "value"}, indent=2)
    """
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=indent)

    return filepath
