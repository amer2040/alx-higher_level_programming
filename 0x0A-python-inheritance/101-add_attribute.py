#!/usr/bin/python3
'''module for add_attribute method'''


def add_attribute(obj, attr, value):
    '''Add new attribute to an object if found.
    Args:
        obj: the object to add an attribute.
        attr: the attribute name.
        value: the value of attr.
    Raise:
        TypeError: If cannot add the attribute
    '''
    if not hasattr(obj, '__dict__'):
        raise TypeError("can't add new attribute")
    setattr(obj, attr, value)
