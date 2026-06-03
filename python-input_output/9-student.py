#!/usr/bin/python3
"""Module to hold Student class"""


class Student():
    """Student class"""
    def __init__(self, first_name, last_name, age):
        """Initialisation function for Student with name and age"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Retrieves dictionary representation of a Student"""
        return self.__dict__
