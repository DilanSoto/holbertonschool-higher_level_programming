#!/usr/bin/python3
""" Square class """
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class inherits from Rectangle class"""
    # constructor

    def __init__(self, size, x=0, y=0, id=None):
        """ init method for square class
        Args:
            size (int): size of the square
            x (int): x position of the square
            y (int): y position of the square
            id (int): id of the square
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ string representation of square """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    # Getters
    @property
    def size(self):
        """ size getter """
        return self.width

    # Setters
    @size.setter
    def size(self, value):
        """ size setter
        Args:
            value (int): value to set size to"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """update method for square class
        Args:
            args (list): list of arguments
            kwargs (dict): dictionary of arguments
        """
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.size = args[1]
            if len(args) >= 3:
                self.x = args[2]
            if len(args) >= 4:
                self.y = args[3]
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """ dictionary representation of square """
        return {'id': self.id, 'size': self.size, 'x': self.x, 'y': self.y}
