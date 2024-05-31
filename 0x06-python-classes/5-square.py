#!/usr/bin/python3

""" class Square that defines a square by: (based on 4-square.py)"""


class Square:
    """redefine suquare class
    """

    def __init__(self, size=0):

        """ constructor
        args:
        size : int private with optional val
        """
        if size != int(size):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        return the area of size
        """
        return self.__size ** 2

    @property
    def size(self):
        """getter of size"""
        return self.__size

    @size.setter
    def size(self, value):
        """ set size val """

        if value != int(value):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        """ prints in stdout the square with the character #
        """
        if self.__size == 0:
            print("")
        else:
            for i in range(self.__size):
                print('#' * self.__size)
