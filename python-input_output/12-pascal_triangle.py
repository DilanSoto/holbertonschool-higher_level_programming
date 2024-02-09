#!/usr/bin/python3
"""
Module that conrains a function that creates a
pascal triangle
"""


def pascal_triangle(n):
    """
    Returns a list of list of integers representing
    that Pascals traingle of n
    """

    if n <= 0:
        return []

    l = [[0 for x in range(i + 1)]for i in range(n)]
    l[0] = [1]

    for i in range(1, n):
        l[i][0] = 1
        for j in range(1, i + 1):
            if j < len(l[i - 1]):
                l[i][j] = l[i - 1][j - 1] + l[i - 1][j]
            else:
                l[i][j] = l[i - 1][0]
    return l
