#!/usr/bin/python3
"""Module for writing to a file by appending"""


def append_write(filename="", text=""):
    """Function to write by appending"""
    with open(filename, "a", encoding="utf-8") as file:
        return file.write(text)
