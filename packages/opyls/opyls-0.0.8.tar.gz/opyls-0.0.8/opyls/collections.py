from typing import Any


# https://www.geeksforgeeks.org/break-list-chunks-size-n-python/
def to_chunks(arr: list[Any], n: int) -> list[list[Any]]:
    """
    Splits a list into chunks of size 'n'.

    Args:
        arr (list[Any]): The list to be chunked.
        n (int): The size of each chunk.

    Returns:
        list[list[Any]]: A list of lists, where each sublist contains 'n' elements
                          from the original list.

    Example:
        >>> to_chunks([1, 2, 3, 4, 5, 6, 7, 8, 9], 3)
        [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    """
    for i in range(0, len(arr), n):
        yield arr[i:i + n]
