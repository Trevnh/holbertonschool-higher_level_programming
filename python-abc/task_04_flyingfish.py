#!/usr/bin/python3
"""Module for Multiple Inheritance"""


class Fish():
    """Class for Fish"""
    def swim(self):
        """Prints The fish is swimming"""
        print("The fish is swimming")

    def habitat(self):
        """Prints The fish lives in water"""
        print("The fish lives in water")

class Bird():
    """Class for Bird"""
    def fly(self):
        """Prints The bird is flying"""
        print("The bird is flying")

    def habitat(self):
        """Prints The bird lives in the sky"""
        print("The bird lives in the sky")

class FlyingFish(Fish, Bird):
    """Class for FlyingFish"""
    def fly(self):
        """Prints The flying fish is soaring!"""
        print("The flying fish is soaring!")

    def swim(self):
        """Prints The flying fish is swimming!"""
        print("The flying fish is swimming!")

    def habitat(self):
        """Prints The flying fish lives both in water and the sky!"""
        print("The flying fish lives both in water and the sky!")
