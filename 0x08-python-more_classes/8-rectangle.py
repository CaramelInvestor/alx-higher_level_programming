#!/usr/bin/python3
"""
This module defines a rectangle by: (based on 0-rectangle.py)
"""


class Rectangle:
    """
    initialized Rectangle cls
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        init method to initialze variables
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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
        str_rep = ""
        if self.width == 0 or self.height == 0:
            return ""
        for _ in range(self.height):
            str_rep += str(self.print_symbol) * self.width
            if _ + 1 < self.__height:
                str_rep += '\n'
        return str_rep

    def __repr__(self):
        """
        Return the string representation of the Rectangle.
        """
        rect = "Rectangle(" + str(self.__width)
        rect += ", " + str(self.__height) + ")"
        return rect

    def __del__(self):
        """
        Print the message when an instance of Rectangle is deleted
        """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        Static method that returns the biggest rectangle based on the area
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError('rect_1 must be an instance of Rectangle')
        if not isinstance(rect_2, Rectangle):
            raise TypeError('rect_2 must be an instance of Rectangle')
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2
