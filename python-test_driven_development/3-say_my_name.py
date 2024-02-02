#!/usr/bin/python3
""" 3. Say my name
Function that prints My name is <first name> <last name>
Raise a TypeError exception if first_name or last_name are not strings
"""


def say_my_name(first_name, last_name=""):
    """ This function prints My name is <first name> <last name>
    Raise a TypeError exception if first_name or last_name are not strings
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
