#!/usr/bin/python3
"""
This module contains a function named
from_json_string that returns an object
represented by a JSON string
"""


import json


def from_json_string(my_str):
    """
    This function returns an objects
    represented by a JSON string
    """
    return json.loads(my_str)
