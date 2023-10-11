#!/usr/bin/python3
'''module for functions'''
import sys

sv_to_json = __import__('5-save_to_json_file').save_to_json_file
ld_from_json = __import__('6-load_from_json_file').load_from_json_file


args = list(sys.argv[1:])

try:
    data = ld_from_json('add_item.json')
except Exception:
    data = []

data.extend(args)
sv_to_json(data, 'add_item.json')
