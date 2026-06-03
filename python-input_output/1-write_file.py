#!/usr/bin/python3
"""Module for writing file"""


def write_file(filename="", text=""):
    """Function for writing file"""
    with open(filename, "w", encoding="utf-8") as file:
        return file.write(text)
