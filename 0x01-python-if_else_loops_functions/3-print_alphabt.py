#!/usr/bin/python3
for x in range(ord('a'), ord('z') + 1):
    if x == 'q' or x == 'e':
        continue
    else:
        print('{:c}'.format(x), end='')
