#!/usr/bin/python3
def no_c(my_string):
    copy = [i for i in my_string if i != 'c' and i != 'C']
    return ("".join(copy))
