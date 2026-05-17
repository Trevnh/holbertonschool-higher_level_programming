#!/usr/bin/python3
"""Module to print text with 2 new lines after . ? and :"""


def text_indentation(text):
    """Function to print text with 2 new lines after . ? and :"""
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    for char in ".?:":
        text = text.replace(char, char + "\n\n")
    print("\n".join(line.strip() for line in text.split("\n")), end="")
