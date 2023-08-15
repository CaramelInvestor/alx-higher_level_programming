#!/usr/bin/python3
"""
This module inherits a class of BaseGeometry (7-base_geometry.py)
"""


BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """
    This class is an inherent class of BaseGeomtry
    """
    def __init__(self, width, height):
        """
        Instantiation method of private attributes
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__width = width
        self.__height = height
