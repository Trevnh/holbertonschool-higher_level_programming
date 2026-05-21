#!/usr/bin/python3
"""Module to contain Rectangle class"""


class Rectangle():
    """Rectangle class"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initialize a Rectangle with height and width"""
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

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
        """Returns a Rectangle made of #s"""
        square = ""
        if self.height == 0 or self.width == 0:
            return square
        for row in range(self.height):
            if row != self.height - 1:
                square += (str(self.print_symbol) * self.width + "\n")
            else:
                square += (str(self.print_symbol) * self.width)
        return square

    def __repr__(self):
        """Returns a representation of a Rectangle"""
        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        """Prints a message when the Rectangle is deleted"""
        print("Bye rectangle...")
        type(self).number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Returns the bigger rectangle based on area"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """Returns a Rectangle with width == height == size"""
        return cls(size, size)
