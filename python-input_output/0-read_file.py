#!/usr/bin/python3
"""
This module have a function called read_file,
that reads and prints a file that it have been past
"""


def read_file(filename=""):
    """
    This function that read a text file
    and prints it to stdout
    """
    with open(filename, 'r') as fd:
        for line in fd:
            print(line, end="")
