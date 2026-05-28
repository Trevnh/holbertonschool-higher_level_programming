#!/usr/bin/python3
"""Module for Verbose List"""


class VerboseList(list):
    """Verbose List class for extra notifications"""
    def append(self, item):
        """Appends a value to the end of the list"""
        super().append(item)
        print(f"Added [{item}] to the list.")

    def extend(self, item):
        """Extends the list with given item"""
        super().extend(item)
        print(f"Extended the list with [{len(item)}] items.")

    def remove(self, item):
        """Removes item from the list"""
        print(f"Removed [{item}] from the list.")
        super().remove(item)

    def pop(self, idx=-1):
        """Pops item at given index from the list"""
        print(f"Popped [{self[idx]}] from the list.")
        return super().pop(idx)
