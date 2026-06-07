#!/usr/bin/python3
"""Module for Basic Serialization"""

import json


def serialize_and_save_to_file(data, filename):
    """Function to Serialize an object and save it to filename"""
    with open(filename, "w") as file:
        return file.write(json.dumps(data))

def load_and_deserialize(filename):
    """Function to load data from a file"""
    with open(filename, "r") as file:
        return json.loads(file.read())
