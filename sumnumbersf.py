#!/usr/bin/python
#sumnumbersf.py
#python program to print sum of first hundred natural numbers using function.

def sumn(n):
    sum = 0
    for i in range(n):
	sum = sum + i 
    print sum
sumn(101)
