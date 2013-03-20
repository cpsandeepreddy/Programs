#!/usr/bin/python
#triangle1.py
#python program to print triangle using class and functions.

class triangle:
    def __init__(self):
        pass
    def first(self,n):
        l = (n - 1) * ' '
	print l + '*'
    def second(self,n):
	k = 1
	p = n - 2
	for i in range(n -1):
	    print p * ' ' + '*' + ((2*k) -1) * ' ' + '*'
	    p -= 1
	    k += 1
    def third(self,n):
	for j in range(n):
            print '*',
t=triangle()
t.first(10)
t.second(10)
t.third(10)

