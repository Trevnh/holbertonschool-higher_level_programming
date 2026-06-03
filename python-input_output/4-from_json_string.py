#!/usr/bin/python3
"""Module for returning an object from a JSON string"""

import json


def from_json_string(my_str):
    """Function to return an object from JSON string"""
    return json.loads(my_str)
