#!/usr/bin/python3
"""
This module contains a function call
lookup that returns a list of availables
attributes and method of the pass object
"""


def lookup(obj):
    """
    This function returns a list of availables
    attributes and methos of an object
    passed to the function.
    """
    return dir(obj)
