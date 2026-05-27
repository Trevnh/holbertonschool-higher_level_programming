#!/usr/bin/python3
"""Module for is_same_class"""


def is_same_class(obj, a_class):
    """Function that returns True if obj is exactly and instance of a_class"""
    return True if type(obj) is a_class else False
