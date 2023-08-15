#!/usr/bin/python3
"""
This module raises an exception
"""


class BaseGeometry:
    """
    A baseGeometry class that raises an exception
    """
    def area(self):
        raise Exception("area() is not implemented")
