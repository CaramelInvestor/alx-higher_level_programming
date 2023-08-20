#!/usr/bin/python3
"""
module to define a base class
"""
import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        method that returns the JSON string representation
        of list_dictionaries
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        method that writes the JSON string representation of
        list_objs to a file
        """
