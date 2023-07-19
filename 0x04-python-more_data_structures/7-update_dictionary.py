#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    if key in a_dictionary:
        a_dictionary[key] = value
        return a_dictionary
    elif isinstance(key, str) and not len(key) == 0:  # check if key=str&!NULL
        new_entry = {key: value}
        a_dictionary.update(new_entry)
        return a_dictionary
