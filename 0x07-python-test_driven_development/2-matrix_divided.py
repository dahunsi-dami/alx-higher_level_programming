#!/usr/bin/python3
"""
Module to divide all elements of a matrix
"""


def matrix_divided(matrix, div):
    """Returns new matrix with all elements in old matrix divided."""

    msg = "matrix must be a matrix (list of lists) of integers/floats"
    if type(matrix) is not list:
        raise TypeError(msg)

    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    lent = len(matrix[0])
    for row in matrix:
        if type(row) is not list:
            raise TypeError(msg)

        if lent != len(row):
            raise TypeError("Each row of the matrix must have the same size")
        for item in row:
            if type(item) is not int and type(item) is not float:
                raise TypeError(msg)

    return [[round(item / div, 2) for item in row] for row in matrix]
