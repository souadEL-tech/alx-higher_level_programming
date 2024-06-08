#!/usr/bin/python3


def add_integer(a, b=98):

    """
    function that adds 2 integers:

    args:
    -----
    a : int or float
    b : int ofr float

    REturn:
    ------
    return the result of addetion
    """

    # variables
    result = 0

    # check args type
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    elif not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    # cast float to int
    if isinstance(a, float):
        a = int(a)
    if isinstance(a, float):
        b = int(b)

    result = a + b

    return (result)
