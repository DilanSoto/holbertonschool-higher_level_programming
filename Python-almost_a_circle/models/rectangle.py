#!/usr/bin/python3
""" Rectangle class """
from models.base import Base


class Rectangle(Base):
    """ Rectangle class inherits from Base class """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ init method for rectangle class
        Args:
            width (int): width of the rectangle
            height (int): height of the rectangle
            x (int): x position of the rectangle
            y (int): y position of the rectangle
            id (int): id of the rectangle
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    """artgument getters"""

    @property
    def width(self):
        """ width getter """
        return self.__width

    @property
    def height(self):
        """ height getter """
        return self.__height

    @property
    def x(self):
        """ x getter """
        return self.__x

    @property
    def y(self):
        """ y getter """
        return self.__y

    """Argument setters """

    @width.setter
    def width(self, value):
        """ width setter
        Args:
            value (int): value to set
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """ height setter
        Args:
            value (int): value to set
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @x.setter
    def x(self, value):
        """ x setter
        Args:
            value (int): value to set
        """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @y.setter
    def y(self, value):
        """ y setter
        Args:
            value (int): value to set
        """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    # Methods
    def area(self):
        """Calculate the area of a rectangle
        Returns:
            The area of the Rectangle
        """
        return self.width * self.height

    def display(self):
        """display the Rectangle using '#' """
        for i in range(self.y):
            print()
        for i in range(self.height):
            for j in range(self.x):
                print(" ", end="")
            for j in range(self.width):
                print("#", end="")
            print()

    def __str__(self):
        """return the string representation of the Rectangle """
        return (f"[Rectangle] ({self.id}) "
                f"{self.x}/{self.y} - {self.width}/{self.height}")

    def update(self, *args, **kwargs):
        """Update the rectangle"""
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.width = args[1]
            if len(args) >= 3:
                self.height = args[2]
            if len(args) >= 4:
                self.x = args[3]
            if len(args) >= 5:
                self.y = args[4]
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """return the dictionary representation of a Rectangle"""
        return {'id': self.id, 'width': self.width, 'height': self.height,
                'x': self.x, 'y': self.y}
