#!/usr/bin/python3
"""
Module to divide all elements of a matrix
"""


def matrix_divided(matrix, div):
    """Returns new matrix with all elements in old matrix divided."""

    if type(matrix) is not list:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    rlen = len(matrix[0])
    for row in matrix:
        if type(row) is not list:
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

        if len(row) != rlen:
            raise TypeError("Each row of the matrix must have the same size")

        if type(div) is not int and type(div) is not float:
            raise TypeError("div must be a number")

        if div == 0:
            raise ZeroDivisionError("division by zero")

    return [[round(item / div, 2) for item in row] for row in matrix]
