#!/usr/bin/python3
'''modules'''


from sys import stdin


status_codes = {
        '200': 0,
        '301': 0,
        '400': 0,
        '401': 0,
        '403': 0,
        '404': 0,
        '405': 0,
        '500', 0
        }

total_size = x = 0


def print_statistics():
    '''prints the statistics'''
    print('File sizr: {}'.format(total_size))
    for key, value in sorted(status_codes.items()):
        if value > 0:
            print('{:s}: {:d}'.format(key, value))

try:
    for line in stdin:
        splitted_line = line.split()
        if len(splitted_line) >= 2:
            status = splitted_line[-2]
            total_size += int(splitted_line[-1])
            if status in status_codes:
                status_codes[status] += 1
        x += 1

        if x % 10 == 0:
            print_statistics()
    print_statistics()
except KeyboardInterrupt as e:
    print_statistics()
