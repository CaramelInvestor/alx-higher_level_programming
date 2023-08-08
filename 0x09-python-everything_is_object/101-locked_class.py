#!/usr/bin/python3
"""
This module defines a LockedClass with no class or object attribute,
that prevents the user from dynamically creating new instance attributes,
except if the new instance attribute is called first_name
"""


class LockedClass:
    """
    class created __slots__ is used to prevent the dynamic creation of attributes
    """
    __slots__ = ["first_name"]
