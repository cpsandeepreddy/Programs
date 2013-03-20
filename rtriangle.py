#!/usr/bin/python
#rtriangle.py
#python program to print rectangle with two triangles.

class triangle:
    def __init__(self):
        pass
    def first(self,n):
        print '*'
    def second(self,n):
        k = 0
        for i in range(n -1):
            print '*' + k * ' ' + '*'
            k += 1
    def third(self,n):
        for j in range((n/2)+1):
            print '*',
t=triangle()
t.first(10)
t.third(10)
t.second(10)
t.third(10)

