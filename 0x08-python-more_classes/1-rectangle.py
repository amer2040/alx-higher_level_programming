#!/usr/bin/python3
"""Define Rectangle Class"""


class Rectangle:
    """Representation of a Rectangle"""
    def __init__(self, width=0, height=0):
        """Initializes the Rectangle"""
        self.height = height
        self.width = width

    @property
    def width(self):
        """get for the private instance attr width"""
        return self.__width

    @width.setter
    def width(self, value):
        """set for the private instance attr width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """get for the private instance attr height"""
        return self.__height

    @height.setter
    def height(self, value):
        """set for the private instance attr height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
