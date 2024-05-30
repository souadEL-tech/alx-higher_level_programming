#!/usr/bin/python3

"""class Square that defines a square by: (based on 0-square.py"""


class Square:

    """redefine suquare class
    """

    def __init__(self, size=0):
        """ constructor
        args:
        size : int private with optional val
        """
        try:
            self.__size = size
        except TypeError as e:
            print("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
