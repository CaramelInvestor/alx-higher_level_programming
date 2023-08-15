#!/usr/bin/python3
"""
This module returns True if the object is an instance of a class that
inherited (directly or indirectly) from the specified class
; otherwise False
"""


def inherits_from(obj, a_class):
    """
    the object is an instance of a class that inherited (directly or
    indirectly) obj: an object
    a_class: a class
    returns None
    """
    return type(obj) != a_class and isinstance(obj, a_class)
