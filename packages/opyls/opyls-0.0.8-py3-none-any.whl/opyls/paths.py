from pathlib import Path
from typing import Optional


def basedir(suffix: Optional[str] = None, mkdir: bool = False) -> Path:
    """
    Get the base directory path.

    Args:
        suffix (Optional[str]): Optional suffix to append to the base directory path.
        mkdir (bool): If True, creates the directory if it does not exist.

    Returns:
        Path: The base directory path.

    Example:
        basedir(suffix="data", mkdir=True)
    """
    base_dir = Path.cwd()

    if suffix is not None:
        base_dir = base_dir / suffix
        if mkdir:
            base_dir.mkdir(exist_ok=True, parents=True)

    return base_dir
