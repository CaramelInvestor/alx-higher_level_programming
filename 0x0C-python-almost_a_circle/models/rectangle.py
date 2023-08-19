#!/usr/bin/python3
"""
The rectangle class inherits from Base class
"""


from models.base import Base


class Rectangle(Base):
    """
    subclass that inherits from the base
    superclass
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Instantiation method to declare private attributes
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """
        getter method for private width attribute
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        setter method for private width attribute
        """
        self.validator("width", value)
        self.__width = value

    @property
    def height(self):
        """
        getter method for private height attribute
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        setter method for private height attribute
        """
        self.validator("height", value)
        self.__height = value

    @property
    def x(self):
        """
        getter method for private x attribute
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        setter method for private x attribute
        """
        self.validator("x", value)
        self.__x = value

    @property
    def y(self):
        """
        getter method for private y attribute
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        setter method for private y attribute
        """
        self.validator("y", value)
        self.__y = value

    @staticmethod
    def validator(attribute, value):
        """
        method that validates all setter methods
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(attribute))
        if attribute == "weight" or attribute == "height":
            if value <= 0:
                raise ValueError("{} must be > 0".format(attribute))
        elif value < 0:
            raise ValueError("{} must be >= 0".format(attribute))

    def area(self):
        """
        method that defines the area of the rectangle
        """
        return self.width * self.height

    def display(self):
        """
        method that prints the rectangle in # char
        """
        for char in range(self.y):
            print()
        for char in range(self.height):
            print(' ' * self.x + '#' * self.width)

    def __str__(self):
        """
        overridding the str method
        """
        return ("[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                self.x, self.y, self.width, self.height))

    def update(self, *args):
        """
        method that assigns an argument to each attribute
        """
        if len(args) == 0:
            for key, val in kwargs.items():
                self.__setattr__(key, val)
            return
        try:
            self.id = args[0]
            self.width = args[1]
            self.height = args[2]
            self.x = args[3]
            self.y = args[4]
        except IndexError:
            pass
