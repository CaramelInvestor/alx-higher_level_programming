#!/usr/bin/python3
"""
This module writes a string to a text file
"""


def write_file(filename="", text=""):
    """
     a function that writes a string to a text file (UTF8) and
     returns the number of characters written
     """
    with open(filename, "w", encoding="utf-8") as f_name:
        num_char = f_name.write(text)
    return num_char
