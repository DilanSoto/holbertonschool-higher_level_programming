#!/usr/bin/python3
"""
This module have a class
that defines a rectangle
"""


class Rectangle:
    """ Definition of rectangle attribute """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """ Initialize by passing a width and a height """
        if type(width) is not int:
            raise TypeError('width must be an integer')
        elif type(height) is not int:
            raise TypeError('height must be an integer')
        elif height < 0:
            raise ValueError('height must be >= 0')
        elif width < 0:
            raise ValueError('width must be >= 0')
        else:
            self.__height = height
            self.__width = width
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
            rec_print += str(self.print_symbol) * self.__width
            if i != self.__height - 1:
                rec_print += "\n"
        return rec_print

    def __repr__(self):
        """ Return string representation of Rectangle """
        return f'Rectangle({self.__width}, {self.__height})'

    def __del__(self):
        """ Messague is printed when an instance is deleted """
        del self
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if isinstance(rect_1, Rectangle) is False:
            raise TypeError('rect_1 must be an instance of Rectangle')
        elif isinstance(rect_2, Rectangle) is False:
            raise TypeError('rect_2 must be an instance of Rectangle')
        elif rect_1.area() > rect_2.area() or rect_1.area() == rect_2.area():
            return rect_1
        elif rect_1.area() > rect_2.area():
            return rect_2
