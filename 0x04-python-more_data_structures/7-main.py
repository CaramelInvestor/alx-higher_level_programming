#!/usr/bin/python3
update_dictionary = __import__('7-update_dictionary').update_dictionary
print_sorted_dictionary = __import__('6-print_sorted_dictionary').print_sorted_dictionary

a_dictionary = { 'name 1': "Ugonma", 'number': 89, 'track': "Low level" }
new_dict = update_dictionary(a_dictionary, 'name', "Pascal")
print_sorted_dictionary(new_dict)
print("--")
print_sorted_dictionary(a_dictionary)

print("--")
print("--")

new_dict = update_dictionary(a_dictionary, 'city', "San Francisco")
new_dict = update_dictionary(a_dictionary, 'Country', "Nigeria")
print_sorted_dictionary(new_dict)
print("--")
print_sorted_dictionary(a_dictionary)
