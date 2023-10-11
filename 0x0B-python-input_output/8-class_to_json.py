#!/usr/bin/python3
'''module for class_to_json method'''


def class_to_json(obj):
    '''returns dict for json serialization of object'''
    return obj.__dict__
