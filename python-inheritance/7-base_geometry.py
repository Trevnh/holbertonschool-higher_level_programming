#!/usr/bin/python3
"""Module for BaseGeometry"""


class BaseGeometry():
    """Class for BaseGeometry"""
    def area(self):
        """Raise an excpetion with a message"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates that value is an integer
        TypeError if value is not int
        ValueError if value is not greater than 0
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
