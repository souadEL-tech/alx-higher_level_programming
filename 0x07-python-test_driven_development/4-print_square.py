#!/usr/bin/python

"""
 a function that prints a square with the character #
"""


def print_square(size):

    """
    args:
    -----
    size: integer > 0

    Raises:
    -------
    Raise valueError if size is less than 0 or float and less than 0
    Raise typeerror if size not integer
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
