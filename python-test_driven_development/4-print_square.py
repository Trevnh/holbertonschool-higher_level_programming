#!/usr/bin/python3
"""Module to print a square of #"""


def print_square(size):
    """Function to print a square of #"""
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if not isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    for i in range(size):
        print(size * "#")
