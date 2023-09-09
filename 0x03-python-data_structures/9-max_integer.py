#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return None
    cp = my_list.copy()
    cp.sort()
    return cp[-1]
