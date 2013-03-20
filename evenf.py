#!/usr/bin/python
#evenf.py
#python program to print even and odd numbers below 100 using function.

def evenodd(n):
    for i in range(n):
        if i%2 == 0:
	    print i,
    for i in range(n):
	if i%2 !=0:
	    print i,
evenodd(100)
