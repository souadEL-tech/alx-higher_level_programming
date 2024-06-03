#!/usr/bin/python3

"""
Write a class Square that defines a square by: (based on 5-square.py)
"""


class Square:

        """
        constructor:
        args:
        size: int
        position: int, int
        """
        def __init__(self, size=0, position=(0, 0)):

            """ about size parameter """
            if size < 0:
                raise ValueError("size must be >= 0")
            elif int(size) != size:
                raise TypeError("size must be an integer")
            self.__size = size

            if position[0] < 0 or position[1] < 0:
                raise TypeError("position must b
                        e a tuple of 2 positive integers")
            else:
                self.__position = position

        """
        getter and setter
        """
        @property
        def size(self):
            return (self.__size)

        @size.setter
        def size(self, value):
            if value < 0:
                raise ValueError("size must be >= 0")
            elif int(value) != value:
                raise TypeError("size must be an integer")
            self.__size = value

        """ getter and setters of position agr"""
        @property
        def position(self):
            return position

        @position.setter
        def position(self, value):
            if value[0] < 0 or value[1] < 0:
                raise TypeError("position must be a tuple of 2 positive integers")
            else:
                self.__position = value

        """ area(self): that returns the current square area"""
        def area(self):
            return (self.__size ** 2)

        """
        my_print(self): that prints in stdout the square with the character #
        """
        def my_print(self):
            if self.__size == 0:
                print("")

            for i in range(self.__size):
                for j in range(self.__position[0]):
                    print("_", end="")
                print("#" * self.__size)
