#!/usr/bin/python
#rectangle1.py
#python program to print rectangle using class and functions.

class rect:
    def __init__(self):
        pass
    def horizontal(self,a):
        for i in range(a):
	    print '*',
    def vertical(self,b):
	for j in range(b):
	    print '*'
    def space(self,a):
        for k in range(a-2):
            print ' ' * (len(range(a-2))-3),


r=rect()
r.horizontal(10)
r.vertical(5),r.space(10)
r.vertical(5)
r.horizontal(10)



