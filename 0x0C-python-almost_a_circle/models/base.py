#!/usr/bin/python3
'''module for Base class'''
from json import loads, dumps
import csv


class Base:
    '''Base class'''

    __nb_objects = 0

    def __init__(self, id=None):
        '''constructor'''
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        '''convert list of dictionaries to json string'''
        if list_dictionaries is None or not list_dictionaries:
            return '[]'
        else:
            return dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        '''convert json string to list of dictionaries'''
        if json_string is None or not json_string:
            return []
        else:
            return loads(json_string)

    @classmethod
    def save_to_files(cls, list_objs):
        '''saves jason object to files'''
        if list_objs is not None:
            list_objs = [x.to_dictionary() for x in list_objs]
        with open(f'{cls.__name__}.json', 'w', encoding='utf-8') as file:
            file.write(cls.to_json_string(list_objs))

    @classmethod
    def load_from_files(cls):
        '''loads json object from files'''
        from os import path
        f = f'{cls.__name__}.json'
        if path.isfile(f):
            return []
        with open(f, 'r', encoding='utf-8') as file:
            return [cls.create(**x) for x in cls.from_json_string(file.read())]

    @classmethod
    def create(cls, **dictionary):
        '''loads instance from dictionary'''
        from models.rectangle import Rectangle
        from models.square import Square
        if cls is Rectangle:
            new = Rectangle(1, 1)
        elif cls is Square:
            new = Square(1)
        else:
            new = None
        new.update(**dictionary)
        return new

    @classmethod
    def save_to_file_csv(cls, list_objs):
        '''save object to csv file'''
        from models.rectangle import Rectangle
        from models.square import Square
        if list_objs is not None:
            if cls is Rectangle:
                list_objs = [[x.id, x.width, x.height, x.x, x.y] \
                             for x in list_objs]
            else:
                list_objs = [[x.id, x.size, x.x, x.y] \
                             for x in list_objs]
        with open(f'{cls.__name__}.csv', 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerows(list_objs)

    @classmethod
    def load_from_file_csv(cls):
        '''loads object from csv file'''
        from models.rectangle import Rectangle
        from models.square import Square
        i = []
        with open(f'{cls.__name__}.csv', 'r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            for row in reader:
                row = [int(r) for r in row]
                if cls is Rectangle:
                    x = {'id': row[0], 'width': row[1], 'height': row[2], \
                        'x': row[3], 'y': row[4]}
                else:
                    x = {'id': row[0], 'size': row[1], \
                         'x': row[2], 'y': row[3]}
                i.append(cls.create(**x))
        return i
