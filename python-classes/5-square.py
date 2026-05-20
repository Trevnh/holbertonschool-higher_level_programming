#!/usr/bin/python3
"""Module to contain Square class"""


class Square():
    """Square Class"""
    def __init__(self, size=0):
        """Initialize a Square with a size"""
        self.size = size

    @property
    def size(self):
        """Gets private instance size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets size to a new value"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Returns the area of a square based on its size"""
        return self.__size**2

    def my_print(self):
        """Prints a square with object size of #"""
        for i in range(self.__size):
            print("#"*self.__size)
        if self.__size == 0:
            print()
