#!/usr/bin/python3

"""
 a function that prints a square with the character #
"""


def print_square(size):

    """Print a square with the # character.

    Args:
        size (int): The height/width of the square.
    Raises:
        TypeError: If size is not an integer.
        ValueError: If size is < 0
    """
    # size's check
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    elif isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")

    # prints a square with the character #.
    for i in range(size):
        print("#" * size)
