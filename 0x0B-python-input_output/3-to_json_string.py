#!/usr/bin/python3
import json
"""
This module converts to JSON string
"""


def to_json_string(my_obj):
    """
    to_json_string function returns the JSON representation
    of an object (string)
    """
    converted_json = json.dumps(my_obj)
    return converted_json
