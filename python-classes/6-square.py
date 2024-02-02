#!/usr/bin/python3
"""" 6. Coordinates of a square
A class Square that defines a square by: (based on 5-square.py)
"""


class Square:
    """Class Square that defines a square"""
    def __init__(self, size=0, position=(0, 0)):
        """Define Private instance attribute: size"""
        self.size = size
        self.position = position

    @property
    def size(self):
        """Private instance attribute: size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Private instance attribute: size"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Private instance attribute: position"""
        return self.__position

    @position.setter
    def position(self, value):
        """Private instance attribute: position"""
        if type(value) is not tuple or len(value) != 2 or \
           type(value[0]) is not int or type(value[1]) is not int or \
           value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Returns the current square area"""
        return self.__size * self.__size

    def my_print(self):
        """Prints in stdout the square with the character #"""
        if self.__size == 0:
            print()
        else:
            for i in range(self.__position[1]):
                print()
            for i in range(self.__size):
                print(" " * self.__position[0], end="")
                print("#" * self.__size)

    def pos_print(self):
        """"Function that returns the position of the square"""

        s_position = ""
        if self.size == 0:
            return "\n"

        for n in range(self.position[1]):
            s_position += "\n"

        for n in range(self.size):
            for x in range(self.position[0]):
                s_position += " "

            for y in range(self.size):
                s_position += "#"

            s_position += "\n"

        return s_position

    def __str__(self):
        """Prints in stdout the square with the character #"""
        return self.pos_print()
