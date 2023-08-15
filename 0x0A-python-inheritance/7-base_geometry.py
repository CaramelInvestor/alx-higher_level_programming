#!/usr/bin/python3
"""
This module raises an exception based on 6-base_geometry.py
"""


class BaseGeometry:
    """
    A baseGeometry class that raises an exception
    """
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        isinstance(name, str)
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value < 0 or value == 0:
            raise ValueError("{} must be greater than 0".format(name))
