#!/usr/bin/python3
"""
module to define a base class
"""


class Base:
    """
    This is the superclass
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Instantiation method for id
        """
        if id is not None and isinstance(id, int):
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
