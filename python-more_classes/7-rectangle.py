#!/usr/bin/python3
"""
This module defines a class Rectangle
"""


class Rectangle:
    """Definition of a Rectangle class"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle instance with width and height"""
        self.width = width  # This will use the width setter
        self.height = height  # This will use the height setter
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Retrieve the width of the Rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the Rectangle"""
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        """Retrieve the height of the Rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of the Rectangle"""
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        """Return the area of the Rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """Return the perimeter of the Rectangle"""
        if self.__height == 0 or self.__width == 0:
            return 0
        return 2 * (self.__height + self.__width)

    def __str__(self):
        """Return the printable representation of the Rectangle"""
        if self.__height == 0 or self.__width == 0:
            return ""
        rec_print = str(self.print_symbol) * self.__width
        return (rec_print + "\n") * (self.__height - 1) + rec_print

    def __repr__(self):
        """Return the string representation of the Rectangle"""
        return f'Rectangle({self.__width}, {self.__height})'

    def __del__(self):
        """Print a message for every deletion of a Rectangle"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
