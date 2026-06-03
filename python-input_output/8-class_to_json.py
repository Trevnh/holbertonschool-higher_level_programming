#!/usr/bin/python3
"""Module that returns dictionary description with simple data structure
for JSON serialization of an object"""


def class_to_json(obj):
    """Return dictionary description of given object"""
    return obj.__dict__
