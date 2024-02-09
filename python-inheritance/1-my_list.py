#!/usr/bin/python3
""""1. My list"""


class MyList(list):
    """"A class MyList that inherits from list"""

    def print_sorted(self):
        """"A function that prints the list, but sorted (ascending sort)"""

        print(sorted(self))
