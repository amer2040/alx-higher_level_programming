#!/usr/bin/python3
'''module for append_after method'''


def append_after(filename="", search_string="", new_string=""):
    '''function inserts a line of text to a file,
    after each line containing a specific string'''
    with open(filename, 'r', encoding='UTF8') as file:
        line_list = []
        while True:
            line = file.readline()
            if line == '':
                break
            line_list.append(line)
            if search_string in line:
                line_list.append(new_string)
    with open(filename, 'w', encoding='UTF8') as file:
        file.writelines(line_list)
