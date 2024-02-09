#!/usr/bin/python3
"""
This module have a class called BaseGeomtry, that
contains two function (area, integer_validator)
"""


class BaseGeometry:
    """
    Class description for Base Geometry
    """
    def area(self):
        """
        Public instance method that raise an Exception
        """
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """
        Public instance method that validates value
        """
        if type(value) is not int:
            raise TypeError(name + " must be an integer")
        elif value <= 0:
            raise ValueError(name + " must be greater than 0")
        else:
            self.name = name
            self.value = value
