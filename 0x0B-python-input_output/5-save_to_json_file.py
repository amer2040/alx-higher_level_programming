#!/usr/bin/python3
'''module to save_to_json_file method'''
import json


def save_to_json_file(my_obj, filename):
    '''writes an Object to a text file, using JSON representation'''
    with open(filename, 'w', encoding='UTF8') as file:
        json.dump(my_obj, file)
