#!/usr/bin/python3

'''Finds all multiples of 2 in a list'''


def divisible_by_2(mylist=[]):
    '''Returns a list of booleans indicating whether or not
    each element in the input list is divisible by 2'''
    new = []
    for i in mylist:
        if i % 2 == 0:
            new.append(True)
        else:
            new.append(False)
    return new
