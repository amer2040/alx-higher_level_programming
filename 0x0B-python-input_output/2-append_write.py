#!/usr/bin/python3
'''module for append_write'''


def append_write(filename="", text=""):
    '''append string at the end of a text file'''
    with open(filename, 'a', encoding='UTF8') as file:
        return file.write(text)
