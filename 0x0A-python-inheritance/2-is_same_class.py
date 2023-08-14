#!/usr/bin/python3
"""
This module returns True if the object is exactly an instance
of the specified class ; otherwise False
"""


def is_same_class(obj, a_class):
    """
    Method to check if obj is an instance of class a_class
    """
    if type(obj) == a_class:
        return True
    else:
        return False
