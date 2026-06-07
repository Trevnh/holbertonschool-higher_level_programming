#!/usr/bin/python3
"""Module for Pascal Triangle"""


def pascal_triangle(n):
    """Function to return a list of lists representing a Pascal Triangle"""
    p_tri = []
    if n <= 0:
        return p_tri
    for i in range(n):
        current = [1]
        for j in range(1, i):
            current.append(p_tri[i - 1][j - 1] + p_tri[i - 1][j])
        if i != 0:
            current.append(1)
        p_tri.append(current)
    return p_tri
