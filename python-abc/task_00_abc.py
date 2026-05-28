#!/usr/bin/python3
"""Module for Abstract Animal Class and Subclasses"""


from abc import ABC, abstractmethod


class Animal(ABC):
    """Animal Abstract Class"""
    @abstractmethod
    def sound(self):
        """Return the Animal's sound"""
        pass

class Dog(Animal):
    """Dog Class"""
    def sound(self):
        """Return Dog's Sound"""
        return "Bark"

class Cat(Animal):
    """Cat Class"""
    def sound(self):
        """Return Cat's Sound"""
        return "Meow"
