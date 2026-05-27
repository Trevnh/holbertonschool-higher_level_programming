#!/usr/bin/python3
"""Module for Rectangle class that inherits from BaseGeometry"""


class Rectangle(BaseGeometry):
    """Rectangle Class"""
    def __init__(self, width, height):
        """Initialises a Rectangle with width and height after validation"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
