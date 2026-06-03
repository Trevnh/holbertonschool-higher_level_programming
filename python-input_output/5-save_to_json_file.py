#!/usr/bin/python3
"""Module to write an object to text file using JSON representation"""

import json


def save_to_json_file(my_obj, filename):
    """Function to write an object to text file with JSON"""
    with open(filename, "w", encoding="utf-8") as file:
        return file.write(json.dumps(my_obj))
