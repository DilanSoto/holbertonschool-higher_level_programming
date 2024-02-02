#!/usr/bin/python3
""" A class that defines a square by: (based on 4-square.py)
"""


class Square:
    """Class Square that defines a square"""

    def __init__(self, size=0):
        """Define Private instance attribute: size"""

        self.__size = size
        if type(size) is not int:
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """Returns the current square area"""

        return self.__size * self.__size

    @property
    def size(self):
        """Retrieve the private instance attribute: size"""

        return self.__size

    @size.setter
    def size(self, value):
        """Set the private instance attribute: size"""

        if type(value) is not int:
            raise TypeError("size must be an integer")

        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        """"Functions that prints square with the '#' character"""

        if self.__size == 0:
            print()

        for number in range(self.__size):
            print("#" * self.__size)
