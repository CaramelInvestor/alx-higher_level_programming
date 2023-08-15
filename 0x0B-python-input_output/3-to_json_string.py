#!/usr/bin/python3
"""
This module converts to JSON string
"""


def to_json_string(my_obj):
    """
    to_json_string function returns the JSON representation
    of an object (string)
    """
    my_json = json.dump(my_obj)
    return my_json
