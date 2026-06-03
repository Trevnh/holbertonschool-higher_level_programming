#!/usr/bin/python3
"""Module for Reading File"""


def read_file(filename=""):
    """Function for reading file"""
    with open(filename) as file:
        content = file.read()
        print(content, end="")
