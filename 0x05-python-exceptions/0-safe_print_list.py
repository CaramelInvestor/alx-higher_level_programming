#!/usr/bin/python3
'''Write a function that prints x elements of a list.

Prototype: def safe_print_list(my_list=[], x=0):
	my_list can contain any type (integer, string, etc.)
	All elements must be printed on the same line followed by a new line.
	x represents the number of elements to print
	x can be bigger than the length of my_list
	Returns the real number of elements printed
	You have to use try: / except:
	You are not allowed to import any module
	You are not allowed to use len()'''

def safe_print_list(my_list=[], x=0):
'''function that prints x elements in my_list'''
    idx = 0
    while True:
        try:
            if idx < x:
                print(my_list[idx], end='')
                idx += 1
            else:
                print()
                return idx
        except IndexError:
            print()
            return idx
