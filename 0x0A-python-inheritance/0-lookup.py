#!/usr/bin/python3
"""Nodule for lookup method."""


def lookup(obj):
    """check object given
    Args:
        obj: is object given to list

    Return:
        list: the list of attributes.
    """
    return dir(obj)
