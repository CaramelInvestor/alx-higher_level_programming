#!/usr/bin/python3
def common_elements(set_1, set_2):
    """a function that returns a set of common elements in two sets"""
    common_elements = set() #create an empty set
    common_elements = set_1 & set_2
    return common_elements
