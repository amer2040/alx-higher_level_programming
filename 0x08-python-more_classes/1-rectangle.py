#!/usr/bin/python3
"""Define Rectangle Class"""


class Rectangle:
    """Representation of a Rectangle"""
    def __init__(self, width=0, height=0):
        """Initializes the Rectangle"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """get for the private instance attr width"""
        return self.__width

    @width.setter
    def width(self, value):
        """set for the private instance attr width"""
        if value < 0:
            raise ValueError("width must be >= 0")
        if type(value) is not int:
            raise TypeError("width must be an integer")
        self.__width = value

    @property
    def height(self):
        """get for the private instance attr height"""
        return self.__height

    @height.setter
    def height(self, value):
        """set for the private instance attr height"""
        if value < 0:
            raise ValueError("height must be >= 0")
        if type(value) is not int:
            raise TypeError("height must be an integer")
        self.__height = value
