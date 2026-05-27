#!/usr/bin/python3
"""Module for MyList inheriting from list"""


class MyList(list):
    """Class that inherits from list and has a sorted print method"""
    def print_sorted(self):
        """Sorted Print Method"""
        print(sorted(self))
