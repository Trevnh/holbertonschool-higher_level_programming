#!/usr/bin/python3
"""Module to contain Rectangle class"""


class Rectangle():
    """Rectangle class"""
    def __init__(self, width=0, height=0):
        """Initialize a Rectangle with height and width"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Gets private instance width"""
        return self.__width

    @property
    def height(self):
        """Gets private instance height"""
        return self.__height

    @width.setter
    def width(self, value):
        """Sets width to value"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @height.setter
    def height(self, value):
        """Sets height to value"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """Returns the area of Rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """Returns the perimeter of Rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return self.__width * 2 + self.__height * 2

    def __str__(self):
        """Prints the Rectangle with #s"""
        square = ""
        if self.__height == 0 or self.__width == 0:
            return square
        for row in range(self.__height):
            if row != self.__height - 1:
                square += ("#" * self.__width + "\n")
            else:
                square += ("#" * self.__width)
        return square
