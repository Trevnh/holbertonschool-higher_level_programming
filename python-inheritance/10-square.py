#!/usr/bin/python3
"""Module for Square class that inherits from Rectangle"""


Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """Square Class"""
    def __init__(self, size):
        """Initialises a square with size validated"""
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """Returns the area of the square"""
        return self.__size ** 2
