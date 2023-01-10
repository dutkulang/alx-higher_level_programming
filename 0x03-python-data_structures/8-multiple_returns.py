#!/usr/bin/python3

def multiple_returns(sentence):
    if not sentence:
        first_letter = None
    else:
        first_letter = sentence[0]
    length = len(sentence)

    return (length, first_letter)
