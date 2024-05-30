""" class Square that defines a square by: (based on 2-square.py)"""


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
        """ setter of size"""
        if value != int(value):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
