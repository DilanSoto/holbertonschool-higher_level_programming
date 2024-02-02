#!/usr/bin/python3
""" This module contains a function that divides all elements of a matrix
"""


def matrix_divided(matrix, div):
    """ This function divides all elements of a matrix
    """

    if type(matrix) is not list:
        raise TypeError("mtrix must be mtrix (list/lists) of integers/floats")

    if type(div) not in [int, float]:
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    for i in matrix:
        if type(i) is not list:
            raise TypeError("mtrx must mtrx (list/lists) of integers/floats")

        if len(i) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")

        for j in i:
            if type(j) not in [int, float]:

                raise TypeError("mtrx must mtrx (lists/lists) integers/floats")

    return [[round(j / div, 2) for j in i] for i in matrix]
