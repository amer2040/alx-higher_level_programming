#!/usr/bin/python3
'''module for Student class'''


class Student:
    '''student class'''
    def __init__(self, first_name, last_name, age):
        '''initilaization of student object'''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        '''retrieves dictionary representation of a Student instance
        If attrs is a list of strings, only attribute names contained
        in this list must be retrieved
        Otherwise, all attributes must be retrieved'''
        if attrs is None:
            return self.__dict__

        new_dict = dict()
        for atr in attrs:
            try:
                new_dict[attr] = self.__dict__[attr]
            except Exception:
                pass
        return new_dict
