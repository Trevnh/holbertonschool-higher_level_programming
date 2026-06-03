#!/usr/bin/python3
"""Module turning objects to json string"""

import json


def to_json_string(my_obj):
    """Function to return json reperesentation of object"""
    return json.dumps(my_obj)
