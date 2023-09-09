#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for s in matrix:
        if len(s) == 0:
            print()
        for x in range(len(s)):
            print('{:d}'.format(s[x]), end='\n' if x is len(s) - 1 else ' ')
