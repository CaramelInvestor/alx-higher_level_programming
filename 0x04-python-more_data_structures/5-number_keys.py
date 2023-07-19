#!/usr/bin/python3
def number_keys(a_dictionary):
    if a_dictionary is not None:
        # return len(a_dictionary.keys())
        sum = 0
        for keys in a_dictionary:
            sum += 1
        return sum
