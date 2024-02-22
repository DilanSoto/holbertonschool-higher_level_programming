#!/usr/bin/python3
"""
This module have a class that defines
a Square, and it inherits from Rectangle
"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Class Square that inherits from Rectangle
    it receive size, x, y and id
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        When initialise she validates value and then
        proceed to assign them.
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ Returns [Square] (id) x/y - size """
        return (f'[Square] ({self.id}) {self.x}/{self.y} - {self.width}')

    @property
    def size(self):
        """
        Return the size of the sqr using
        the width of the upper class
        """
        return super().width

    @size.setter
    def size(self, size):
        """ Sets the sqr size """
        self.width = size

    def update(self, *args, **kwargs):
        """
        Assigns the attribute, if args is empty
        then it used the kwards to assign
        """
        if args is not None:
            count = 0
            for arg in args:
                if count == 0:
                    self.id = arg
                if count == 1:
                    self.width = arg
                if count == 2:
                    self.x = arg
                if count == 3:
                    self.y = arg
                count += 1

        for key, elem in kwargs.items():
            if key == "id":
                self.id = elem
            if key == "size":
                self.width = elem
            if key == "x":
                self.x = elem
            if key == "y":
                self.y = elem

    def to_dictionary(self):
        """
        Dictionaty representation of the class
        """
        dic_sqr = {
            'id': self.id,
            'size': self.width,
            'x': self.x,
            'y': self.y
        }
        return dic_sqr
