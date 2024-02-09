#!/usr/bin/python3
"""
This module have a function named append_write
that appends the text given to the file
"""


def append_write(filename="", text=""):
    """
    This function appends a tring at the
    end of a text file and return the number
    of characters added
    """
    with open(filename, 'a') as fd:
        return fd.write(text)
