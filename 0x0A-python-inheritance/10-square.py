#!/usr/bin/python3
'''module for Square class'''
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    '''Square subclass'''
    def __init__(self, size):
        '''constructor'''
        self.integer_validator('size', size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        '''area method of square'''
        return self.__size ** 2
