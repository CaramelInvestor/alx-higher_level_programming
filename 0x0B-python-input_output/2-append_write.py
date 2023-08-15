#!/usr/bin/python3
"""
This module appends text to a file
"""


def append_write(filename="", text=""):
    """
    function that appends a string at the end of a text file
    (UTF8) and returns the number of characters added
    """
    with open(filename, "a", encoding="utf-8") as f_name:
        num_char = f_name.write(text)
    return num_char
