from configparser import ConfigParser
from pathlib import Path
from typing import Union, Any

import json


# https://www.postgresqltutorial.com/postgresql-python/connect/
def load_ini(filename: Union[str, Path], section: str) -> dict[str, str]:
    """
    Load configuration from an INI file.

    Args:
        filename (str): The path to the INI file.
        section (str): The name of the section to load.

    Returns:
        Dict[str, str]: A dictionary containing the configuration parameters.

    Raises:
        Exception: If the specified section is not found in the INI file.

    Example:
        load_ini("config.ini", "section_name")
    """
    parser = ConfigParser()
    parser.read(filename)

    config = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            config[param[0]] = param[1]
    else:
        raise Exception('Section {0} not found in the {1} file'.format(section, filename))

    return config


def load_json(filename: Union[str, Path]) -> Any:
    """
    Load JSON data from a file.

    Args:
        filename (Union[str, Path]): The path to the JSON file.

    Returns:
        Any: The deserialized JSON data.

    Example:
        load_json("data.json")
    """
    with open(filename, 'r') as f:
        return json.load(f)
