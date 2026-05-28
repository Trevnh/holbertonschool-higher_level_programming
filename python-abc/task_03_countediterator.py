#!/usr/bin/python3
"""Module for CountedIterator"""


class CountedIterator():
    """Counted Iterator class"""
    def __init__(self, iterable):
        """Initialise the iterator and count to 0"""
        self.iterator = iter.(iterable)
        self.count = 0

    def get_count():
        """Return the count"""
        return self.count

    def __next__(self):
        """Return the next item and increment count by 1"""
        item = next(self.iterator)
        self.count += 1
        return item
