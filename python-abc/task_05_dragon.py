#!/usr/bin/python3
"""Module for Mixins"""


class SwimMixin():
    """Swim Mixin to include swim()"""
    def swim(self):
        """Prints The creature swims!"""
        print("The creature swims!")

class FlyMixin():
    """Fly Mixin to include fly()"""
    def fly(self):
        """Prints The creature flies!"""
        print("The creature flies!")

class Dragon(SwimMixin, FlyMixin):
    """Dragon Class"""
    def roar(self):
        """Prints The dragon roars!"""
        print("The dragon roars!")
