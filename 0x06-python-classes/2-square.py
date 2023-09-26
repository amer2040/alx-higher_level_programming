#!/usr/bin/python3
"""Square modules"""


class Square:
    """Define a square"""

    def __init__(self, size=0):
        """Constructor.

        Args:
            size: length of a side os the square.

        Raises:
            TypeError: if size is not an integer.
            ValueError: if size is less than Zero.
        """
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size
