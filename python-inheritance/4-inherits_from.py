#!/usr/bin/python3
"""
This module contains a function called
inhertis_from that returns True or False
"""


def inherits_from(obj, a_class):
    """
    This function returns True if the object is
    and instance of a class that inherited from
    the specified class; otherwise False
    """
    if isinstance(obj, a_class) and type(obj) is not a_class:
        return True
    else:
        return False
