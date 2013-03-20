#!/usr/bin/python
#triangle.py
#python program to print triangle.

def triangle(n):
    l = (n - 1) * ' '
    print l + '*' 
    k = 1
    p = n - 2
    for i in range(n - 1):
	print p * ' ' + '*' + ((2 * k) - 1) * ' ' + '*'
        p -= 1
	k += 1
    for j in range(n):
	print '*',
triangle(10) 
        
