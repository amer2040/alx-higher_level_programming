#!/usr/bin/python3
for x in range(ord('A'), ord('Z') + 1):
    if x != ord('Z'):
        print('{:c}'.format(x), end='')
    else:
        print('Z')
