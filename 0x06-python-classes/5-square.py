#!/usr/bin/python3
"""Square modules"""


class Square:
    """Define a square"""

    def __init__(self, size=0):
        """Constructor.

        Args:
            size: length of a side os the square.
        """
        self.__size = size

    @property
    def size(self):
        """property for the length of a side of square.

        Raises:
            TypeError: if size is not an integer.
            ValueError: if size is less than Zero.
        """
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        """Public instance method calculate Square Area.

        Returns: The size * itslef.
        """
        return self.__size ** 2

    def my_print(self):
        """prints the square"""
        for x in range(self.size):
            for y in range(self.size):
                print('#', end='\n' if y is self.size - 1 and x != y else "")
        print()
