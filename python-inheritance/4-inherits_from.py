#!/usr/bin/python3
"""Module for inherits_from"""


def inherits_from(obj, a_class):
    """Check if obj inherits from a_class
    but is not directly a_class
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
