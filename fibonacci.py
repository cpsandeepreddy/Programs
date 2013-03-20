#!/usr/bin/python
#fibonacci.py
#python program to print the fibonacci series.

def f(n):
    a, b = 0, 1
    while b < n:
        print b,
        a, b = b, a + b
f(n = int(raw_input("print integer value:")))
        
      

