#!/usr/bin/python3
""" Base class """
from os import path
import json
import turtle


class Base:
    """atts for the base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """init method for base class
        Args:
            id (int): id of the object
            """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    """class methods"""

    @classmethod
    def load_from_file(cls):
        """ class method to return list of instances """
        import json
        filename = cls.__name__ + ".json"
        list_dict = []
        try:
            with open(filename, 'r') as f:
                list_dict = cls.from_json_string(f.read())
        except FileNotFoundError:
            pass
        list_inst = []
        for dict in list_dict:
            list_inst.append(cls.create(**dict))
        return list_inst

    @classmethod
    def create(cls, **dictionary):
        """ class method to return instance with attributes already set
        Args:
            dictionary (dict): dictionary of attributes
        """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        cls.update(dummy, **dictionary)
        return dummy

    @classmethod
    def save_to_file(cls, list_objs):
        """ class method to write json string to file
        Args:
            list_objs (list): list of objects
        """
        filename = cls.__name__ + ".json"
        list_dict = []
        if list_objs is not None:
            for obj in list_objs:
                list_dict.append(obj.to_dictionary())
        with open(filename, 'w') as f:
            f.write(cls.to_json_string(list_dict))

    """static methods"""

    @staticmethod
    def to_json_string(list_dictionaries):
        """ static method to return json string representation
        Args:
            list_dictionaries (list): list of dictionaries
        """
        if list_dictionaries is None or list_dictionaries is []:
            return "[]"
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        if json_string is None or json_string is []:
            return []
        return json.loads(json_string)

    @staticmethod
    def draw(list_rectangles, list_squares):
        """ static method to draw all Rectangles and Squares """
        # Create a turtle object
        t = turtle.Turtle()

        # Set the turtle speed and pen size
        t.speed(0)
        t.pensize(2)
        # Draw all the Rectangles
        for rect in list_rectangles:
            t.penup()
            t.goto(rect.x, rect.y)
            t.pendown()
            t.color("pink")
            for i in range(2):
                t.forward(rect.width)
                t.left(90)
                t.forward(rect.height)
                t.left(90)

        # Draw all the Squares
        for square in list_squares:
            t.penup()
            t.goto(square.x, square.y)
            t.pendown()
            t.color("violet")
            for i in range(4):
                t.forward(square.size)
                t.left(90)

        # Exit the turtle graphics window
        turtle.done()
