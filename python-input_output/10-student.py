#!/usr/bin/python3
""" This module contains the class Student """


class Student:
    """ Declaration of class Students """
    def __init__(self, first_name, last_name, age):
        """ Initialize the class """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation
        of the Student class
        """
        if attrs is not None:
            new_dict = {}
            for i in attrs:
                if str(i) == "first_name":
                    new_dict[i] = self.first_name
                elif i == "last_name":
                    new_dict[i] = self.last_name
                elif i == "age":
                    new_dict[i] = self.age
            return new_dict
        else:
            return self.__dict__
