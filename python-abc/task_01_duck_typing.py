#!/usr/bin/python3
"""Module for Duck Typing"""


from abc import ABC, abstractmethod
from math import pi

class Shape(ABC):
    """Abstract Class Shape"""
    @abstractmethod
    def area(self):
        """Return the Shape's area"""
        pass

    def perimeter(self):
        """Return the Shape's perimeter"""
        pass

class Circle(Shape):
    """Circle Class"""
    def __init__(self, radius):
        """Initialise a Circle with given radius"""
        self.__radius = radius

    def area(self):
        """Returns the area of the Circle"""
        return pi * abs(self.__radius) ** 2

    def perimeter(self):
        """Returns the perimeter of the Circle"""
        return 2 * pi * abs(self.__radius)

class Rectangle(Shape):
    """Rectangle Class"""
    def __init__(self, width, height):
        """Initialise a Rectangle with given width and height"""
        self.__width = width
        self.__height = height

    def area(self):
        """Returns the area of the Rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """Returns the perimeter of the Rectangle"""
        return (2 * self.__width) + (2 * self.__height)

def shape_info(shape):
    """Prints the area and perimeter of given shape"""
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")
