#!/usr/bin/python3
"""Module for serializing and deserializing with pickle method"""

import pickle


class CustomObject():
    """Custom Object class"""
    def __init__(self, name, age, is_student):
        """Initialize CustomObject instance with given data"""
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Print the CustomObject attributes"""
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """Serialize with pickle"""
        with open(filename, "wb") as file:
            return pickle.dump(self, file)

    @classmethod
    def deserialize(cls, filename):
        """Deserialize with pickle"""
        with open(filename, "rb") as file:
            return pickle.load(file)
