#!/usr/bin/python
#python program to print multiplication of first 10 numbers start with 3 using reduce function.

def f(n):
    def f1(a,b):
        return a*b
    print reduce(f1,range(1,n),3)
f(11)
