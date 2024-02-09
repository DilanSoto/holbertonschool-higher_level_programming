#!/usr/bin/python3
"""
This module have a function named write_file
that writes in the filed given to us
"""


def write_file(filename="", text=""):
    """
    This function that write a
    string to a text file and
    return the number of character
    written
    """
    with open(filename, 'w') as fd:
        return fd.write(text)
