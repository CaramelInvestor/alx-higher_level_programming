#!/usr/bin/python3
"""
The rectangle class inherits from Base class
"""


Base = __import__('base.py').Base


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
	def width(self, width):
		"""
		getter method for private width attribute
		"""
		return self.__width

	@width.setter
	def width(self, width):
		"""
		setter method for private width attribute
		"""
		self.__width = width

	@property
        def height(self, height):
                """
                getter method for private height attribute
                """
                return self.__height

        @height.setter
        def height(self, height):
                """
                setter method for private height attribute
                """
                self.__height = height

	@property
        def x(self, x):
                """
		getter method for private x attribute
                """
                return self.__x

        @x.setter
        def x(self, x):
                """
                setter method for private x attribute
                """
                self.__x = x

	@property
        def y(self, y):
                """
                getter method for private y attribute
                """
                return self.__y

        @y.setter
        def y(self, y):
                """
                setter method for private y attribute
                """
                self.__y = y
