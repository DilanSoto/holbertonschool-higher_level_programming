#!/usr/bin/python3
"""
This module defines a Rectangle class.
"""

class Rectangle:
    """Definition of a rectangle."""

    number_of_instances = 0  # Initialize class attribute here
    print_symbol: any = "#"  # Type hint for print_symbol

    def __init__(self, width=0, height=0):
        """Initialize a rectangle with optional width and height."""
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__width = width
        self.__height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """ Return the width of the rectangle """
        return self.__width

    @width.setter
    def width(self, value):
        """ Sets the with of the rectangle """
        if type(value) is not int:
            raise TypeError('width must be an integer')
        elif value < 0:
            raise ValueError('width must be >= 0')
        else:
            self.__width = value

    @property
    def height(self):
        """ Return the height of the rectangle """
        return self.__height

    @height.setter
    def height(self, value):
        """ Sets the height of the rectangle """
        if type(value) is not int:
            raise TypeError('height must be an integer')
        elif value < 0:
            raise ValueError('height must be >= 0')
        else:
            self.__height = value

    def area(self):
        """ Return the area of the rectangle """
        result_area = self.__width * self.__height
        return result_area

    def perimeter(self):
        """ Return the perimeter of the rectangle """
        if self.__height == 0 or self.__width == 0:
            result_peri = 0
            return result_peri
        else:
            height_total = self.__height + self.__height
            width_total = self.__width + self.__width
            result_peri = height_total + width_total
        return result_peri

    def __str__(self):
        """ Prints the rectangle shape """
        if self.__height == 0 or self.__width == 0:
            return ""
        rec_print = ""
        for i in range(self.__height):
            rec_print += "#" * self.__width
            if i != self.__height - 1:
                rec_print += "\n"
        return rec_print

    def __repr__(self):
        """ Return string representation of Rectangle """
        return f'Rectangle({self.__width}, {self.__height})'

    def __del__(self):
        del self
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
