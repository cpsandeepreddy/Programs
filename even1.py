#!/usr/bin/python
#python program to print even and odd numbers.

def f(n):
    for i in range(1,n):
        if i%2 == 0:
            print i, 'is a even number'
	    continue
        print i, 'is a odd number'
f(100)
