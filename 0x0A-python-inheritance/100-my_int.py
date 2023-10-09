#!/usr/bin/python3
'''module for MyInt class'''


class MyInt(int):
    '''define MyInt class'''
    def __new__(cls, *args, **kwargs):
        '''new instance of class'''
        return super(MyInt, cls).__new__(cls, *args, **kwargs)

    def __eq__(self, other):
        '''convert from == to !='''
        return int(self) != other

    def __ne__(self, other):
        '''convert != to =='''
        return int(self) == other
