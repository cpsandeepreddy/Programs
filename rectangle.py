#!/usr/bin/python
#rectangle.py
#python program to print rectangle.

def rectangle(a, b):
    for i in range(a):
        print '*',
    for j in range(b):
        print '\n' + '*' + ' ' *((2 * len(range(a))) - 3) + '*'
    for k in range(a):
        print '*',
rectangle(10, 5)
