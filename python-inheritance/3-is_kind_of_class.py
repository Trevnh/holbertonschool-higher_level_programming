#!/usr/bin/python3
"""Module for is_kind_of_class"""


def is_kind_of_class(obj, a_class):
    """Function that returns True
    if obj is an instance or inherited from a_class
    """
    return True if isinstance(obj, a_class) else False
