#!/usr/bin/python3
'''module for write_file method'''


def write_file(filename="", text=""):
    '''write string to text file and returns number of chars written'''
    with open(filename, 'w', encoding='UTF8') as file:
        return file.write(text)
