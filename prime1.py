#!/usr/bin/python
#prime1.py
#python program to print prime numbers.

def f(n):
    for i in range(2, n):
        for j in range(2, i):
            if i%j == 0:
                print i, '=', j, '*', i/j
		break
	else:
	    print i, 'is a prime number'
f(100)
