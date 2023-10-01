#!/usr/bin/python3
"""modules for add_integer method"""

def add_integer(a, b=98):
    """Write a function that adds 2 integers.

    Args:
    a: an integer number
    b: an integer number

    Raise:
    TypeError: if a, b are not int or float
    """

    if type(a) not in (int, float):
        raise TypeError("a must be an integer")
    if type(b) not in (int, float):
        raise TypeError("b must be an integer")
    return int(a) + int(b)

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/0-add_integer.txt")
