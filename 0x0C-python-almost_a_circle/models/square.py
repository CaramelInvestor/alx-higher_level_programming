#!/usr/bin/python3
"""
This square class inherits from Rectangle class
"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """
    subclass Square that inherits from a rectangle subclass
    that iinherits from superclass Base
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        instantiation of superclass attributes
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        method to return string
        """
        return ("[Square] ({:d}) {:d}/{:d} - {:d}".format(self.id,
                self.x, self.y, self.width))

    @property
    def size(self):
        """
        getter method for the square
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        setter method for the width and height of the square
        """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        method to that assigns attributes
        """
        if len(args) >= 1:
            self.id = args[0]
        if len(args) >= 2:
            self.size = args[1]
        if len(args) >= 3:
            self.x = args[2]
        if len(args) >= 4:
            self.y = args[3]

        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)

    def to_dictionary(self):
        """
        public method that returns the dictionary representation of a Square
        """
        return {"id": self.id, "x": self.x, "size": self.size, "y": self.y}
