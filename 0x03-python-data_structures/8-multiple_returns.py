#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence is None:
        sentence[0] = None
    else:
        fc = sentence[0]

    length = len(sentence)
    return(length, fc)
