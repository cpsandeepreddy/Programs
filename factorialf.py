#!/usr/bin/python
#factorialf.py
#python program to print factorial of 100 using function.

fact = 1
def fac(n):
    for i in range(n):
        fact = fact * i
        print fact
fac(10)


