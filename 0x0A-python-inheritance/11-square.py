#!/usr/bin/python3
"""
This module inherits a class of Rectangle (9.rectangle.py)
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    This class is an inherent class of rectangle
    """
    def __init__(self, size):
        """
        Instantiation of private attributes checks if size
        is a positive integer
        """
        self.__size = size
        super().__init__(self.__size, self.__size)

    def __str__(self):
        return ("[Square]" + str(self.__size) + "/" + str(self.__size))
