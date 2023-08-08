#!/usr/bin/python3
"""This module prints a square with the character #."""


def print_square(size):
    """A function that prints a square with the character #.
    size is the size of the length of the square"""
    if not isinstance(size, int):
        raise TypeError('size must be an integer')
    if size < 0:
        raise ValueError('size must be >= 0')
    if isinstance(size, float) and size < 0:
        raise TypeError('size must be an integer')
    for a in range(size):
        print("#" * size)
