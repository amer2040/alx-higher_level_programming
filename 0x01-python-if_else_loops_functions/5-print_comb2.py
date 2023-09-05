#!/usr/bin/python3
for x in range(100):
    if x == 99:
        print('{:02d}'.format(99))
    else:
        print('{:02d}'.format(x), end=', ')
