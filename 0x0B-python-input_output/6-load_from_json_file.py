#!/usr/bin/python3
"""
This module creates an Object
"""
import json


def load_from_json_file(filename):
    """
    function that creates an Object from a “JSON file”
    """
    with open(filename) as f_name:
        return json.load(f_name)
