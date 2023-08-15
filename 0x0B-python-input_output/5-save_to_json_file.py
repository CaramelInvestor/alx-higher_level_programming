#!/usr/bin/python3
"""
This module writes an object to a text file
"""
import json


def save_to_json_file(my_obj, filename):
    """
    function that writes an Object to a text file,
    using a JSON representation
    """
    with open(filename, "w", encoding="utf-8") as f_name:
        return json.dump(my_obj, f_name)
