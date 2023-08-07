#!/usr/bin/python3
"""
This module defines a rectangle by: (based on 0-rectangle.py)
"""


class Rectangle:
    """
    initialized Rectangle cls
    """
    def __init__(self, width=0, height=0):
        """
        init method to initialze variables
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Private instance attribute: width is returned
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        property setter to set it
        """
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        elif value < 0:
            raise ValueError('width must be >= 0')
        else:
            self.__width = value

    @property
    def height(self):
        """
        Private instance attribute: height is returned
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        property setter to set it
        """
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        elif value < 0:
            raise ValueError('height must be >= 0')
        else:
            self.__height = value

    def area(self):
        """
        Public instance method: that returns the rectangle area in
        """
        area = self.width * self.height
        return area

    def perimeter(self):
        """
        Public instance method: that returns the rectangle perimeter in
        """
        perimeter = 2 * (self.width + self.height)
        if self.width == 0 or self.height == 0:
            perimeter = 0
        return perimeter

    def __str__(self):
        """
        Returns a string representation of the rectangle using #
        """
        if self.width == 0 or self.height == 0:
            return ""
        rectangle_str = ""
        for _ in range(self.height):
            rectangle_str += "#" * self.width + "\n"
        return rectangle_str.rstrip()

    def __repr__(self):
        """Return the string representation of the Rectangle."""
        rect = "Rectangle(" + str(self.__width)
        rect += ", " + str(self.__height) + ")"
        return (rect)
