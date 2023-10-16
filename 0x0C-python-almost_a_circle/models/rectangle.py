#!/usr/bin/python3
'''module for Rectangle class'''
from models.base import Base


class Rectangle(Base):
    '''Rectangle class'''

    def __init__(self, width, height, x=0, y=0, id=None):
        '''constructor'''
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        '''get width'''
        return self.__width

    @width.setter
    def width(self, value):
        '''set width'''
        self.validate_integer('width', value, False)
        self.__width = value

    @property
    def height(self):
        '''get height'''
        return self.__height

    @height.setter
    def height(self, value):
        '''set height'''
        self.validate_integer('height', value, False)
        self.__height = value

    @property
    def x(self):
        '''get x'''
        return self.__x

    @x.setter
    def x(self, value):
        '''set x'''
        self.validate_integer('x', value)
        self.__x = value

    @property
    def y(self):
        '''get y'''
        return self.__y

    @y.setter
    def y(self, value):
        '''set y'''
        self.validate_integer('y', value)
        self.__y = value

    def validate_integer(self, name, value, eq=True):
        '''validate the value'''
        if type(value) != int:
            raise TypeError(f'{name} must be an integer')
        elif eq and value < 0:
            raise ValueError(f'{name} must be >= 0')
        elif value <= 0 and not eq:
            raise ValueError(f'{name} must be > 0')

    def area(self):
        '''get area of the rectangle'''
        return self.width * self.height

    def display(self):
        '''print representation of the rectangle in string'''
        string = '\n' * self.y + \
                (' ' * self.x + '#' * self.width + '\n') * self.height
        print(string, end='')

    def __str__(self):
        '''Returns info about the rectangle in string'''
        return f'[{type(self).__name__}] \
                ({self.id}) {self.x}/{self.y} - {self.width}/{self.height}'

    def __update(self, id=None, width=None, height=None, x=None, y=None):
        '''private method to updates instance attributes by */**args'''
        if id is not None:
            self.id = id
        elif width is not None:
            self.width = width
        elif height is not None:
            self.height = height
        elif x is not None:
            self.x = x
        elif y is not None:
            self.y = y

    def update(self, *args, **kwargs):
        '''update instance attributes by keyword args and no-keyword'''
        if args:
            self.__update(*args)
        elif kwargs:
            self.__update(**kwargs)

    def to_dictionary(self):
        '''return dictionary representation of the rectangle'''
        return {
        'id': self.id,
        'width': self.__width,
        'height': self.__height,
        'x': self.__x,
        'y': self.__y
        }
