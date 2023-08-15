#!/usr/bin/python3
"""
This module inherits 9-rectangle.py
"""

Rectangle = __import__('9-rectangle').Rectangle
"""
Square class
"""


class Square(Rectangle):
    """
    A subclass of Rectangle
    """
    def __init__(self, size):
        """
        Instantiation with size
        """
        self.__size = size
        self.integer_validator("size", size)
        super().__init__(self.__size, self.__size)
