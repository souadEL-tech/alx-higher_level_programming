#!/usr/bin/python3


""" class Square that defines a square by: (based on 4-square.py)"""


class Square:
    """redefine suquare class
    """

    def __init__(self, size=0, position=(0, 0)):

        """ constructor
        args:
        size : int private with optional val
        position: int private with optional val
        """

        if size != int(size):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

        if position[0] < 0 or position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = position

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

    @property
    def position(self):
        """position's getter"""
        return self.__position

    @position.setter
    def position(self, value):
        """  position's setter """
        if (value[0] < 0) or 
        (value[1] < 0) or
        value != tuple(value):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def my_print(self):
        """ prints in stdout the square with the character #
        """
        if self.__size == 0:
            print("")
        else:
            for i in range(self.__size):
                for j in range(self.__position[0]):
                    print('_', end="")
                print('#' * self.__size)
