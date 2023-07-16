#!/usr/bin/python3

def multiple_returns(sentence):
    '''returns a tuple containing the
    length and first letter of the sentence'''
    if len(sentence) == 0:
        return(0, None)
    first = sentence[0]
    length = len(sentence)
    return (length, first)
