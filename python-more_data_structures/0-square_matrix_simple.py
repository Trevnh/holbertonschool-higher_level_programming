#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = list(map(list, matrix))
    for i in range(0, len(matrix)):
        new_matrix[i] = list(map(lambda x: x ** 2, matrix[i]))
    return new_matrix
