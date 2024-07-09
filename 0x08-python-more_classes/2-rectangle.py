#!/usr/bin/python3

""" Rectangle class : defines a rectangle by: (based on 1-rectangle.py)"""


class Rectangle:

    """
    class:
    -------
    Rectangle : define Rectangle , calculate  Area and perimeter

    methods:
    --------
    __init__ : method that define width and height
    getter and setters for width and height
    Area : retrurn the Area of the rectangle
    Perimeter: return the perimeter of the rectangle

    Args:
    -----
    width: integer
    height: integer
    """

    def __init__(self, width=0, height=0):

        """ method that define width and height """
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")

        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")

        self.width = width
        self.height = height

    @property
    def width(self):
        """  to get width """
        return (self.__width)

    @width.setter
    def width(self, value):
        """ width setter """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    # about the heigth

    @property
    def height(self):
        """ height getter """
        return (self.__height)

    @height.setter
    def height(self, value):
        """ height setter """

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ Retrun the Area of the rectangle"""
        return (self.__width * self.__height)

    def perimeter(self):
        """ Reteurn the Perimeter of the rectangle """
        return (2 * (self.__width + self.__height))
