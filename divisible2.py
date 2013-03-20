#!/usr/bin/python
#python program to print numbers which are divisible by 2 and 3.

def f(n):
    for i in range(1,n):
        if i%2 == 0 and i%3 == 0:
            print i,
f(int(raw_input('please enter integer vlaue:')))
