#!/usr/bin/python3
"""Module to contain Square class"""


class Square():
    """Square Class"""
    def __init__(self, size=0, position=(0, 0)):
        """Initialize a Square with a size"""
        self.size = size
        self.position = position

    @property
    def size(self):
        """Gets private instance size"""
        return self.__size

    @property
    def position(self):
        """Gets private instance position"""
        return self.__position

    @size.setter
    def size(self, value):
        """Sets size to a new value"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @position.setter
    def position(self, value):
        """Sets position to a new value"""
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not isinstance(value[0], int) or
                not isinstance(value[1], int) or
                value[0] < 0 or
                value[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """Returns the area of a square based on its size"""
        return self.__size**2

    def my_print(self):
        """Prints a square with object size of #"""
        if self.__size == 0:
            print()
            return
        for i in range(self.__position[1]):
            print()
        for i in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
