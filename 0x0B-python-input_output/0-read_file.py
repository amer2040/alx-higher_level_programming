#!/usr/bin/python3
'''module for read_file method'''


def read_file(filename=""):
    '''read_file method'''
    with open(filename, 'r', encoding='UTF8') as file:
        file_read = file.read()

    print(file_read, end='')
