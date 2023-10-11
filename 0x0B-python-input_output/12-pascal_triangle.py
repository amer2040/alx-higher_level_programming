#!/usr/bin/python3
'''module for pascal_triangle method'''


def pascal_triangle(n):
    '''returns a list of lists of integers representing
    the Pascal’s triangle of (n)'''
    if n <= 0:
        return []

    triangles = [[1]]
    while len(triangles) != n:
        tr = triangles[-1]
        temp = [1]
        for x in range(len(tr) - 1):
            temp.append(tr[x] + tr[x + 1])
        temp.append(1)
        triangles.append(temp)
    return triangles
