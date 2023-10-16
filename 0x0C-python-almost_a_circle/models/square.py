#!/usr/bin/python3
'''module for sqaure class'''
from models.rectangle import Rectangle


class Square(Rectangle):
    '''square class'''
    def __init__(self, size, x=0, y=0, id=None):
        '''constructor'''
        super().__init__(size, size, x, y, id)

    def __str__(self):
        '''returns info about the square'''
        return '[{}] ({}) {}/{} - {}'.format(type(self).__name__,
                                             self.id, self.x, self.y,
                                             self.width)

    @property
    def size(self):
        '''get size'''
        return self.width

    @size.setter
    def size(self, value):
        '''set size'''
        self.width = value
        self.height = value

    def __update(self, id=None, size=None, x=None, y=None):
        '''update instance attributes by */**args'''
        if id is not None:
            self.id = id
        if size is not None:
            self.size = size
        if x is not None:
            self.x = x
        if y is not None:
            self.y = y

    def update(self, *args, **kwargs):
        '''update instance attributes by keyword args and no-keyword'''
        if args:
            self.__update(*args)
        if kwargs:
            self.__update(**kwargs)

    def to_dictionary(self):
        '''return dictionary representation of Square'''
        return {
            'id': self.id,
            'size': self.width,
            'x': self.x,
            'y': self.y
        }
