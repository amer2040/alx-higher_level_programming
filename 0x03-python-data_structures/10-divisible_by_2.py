#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if not my_list:
        return None
    div = []
    for x in my_list:
        if (x % 2) == 0:
            div.append(True)
        else:
            div.append(False)
    return div
