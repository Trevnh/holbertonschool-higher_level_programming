#!/usr/bin/python3
"""Module to divide all elements of a matrix"""


def matrix_divided(matrix, div):
    """Function to divide elements of a matrix"""
    if not isinstance(div, (float, int)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if not all(isinstance(element, list) for element in matrix):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats"
        )
    row_size = len(matrix[0])
    new_matrix = []
    for row in matrix:
        if len(row) != row_size:
            raise TypeError(
                "Each row of the matrix must have the same size"
            )
        new_row = []
        for element in row:
            if not isinstance(element, (float, int)):
                raise TypeError(
                    "matrix must be a matrix "
                    "(list of lists) of integers/floats"
                )
            new_row.append(round(element / div, 2))
        new_matrix.append(new_row)
    return new_matrix
