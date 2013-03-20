#!/usr/bin/python
#primef.py
#python program to print prime numbers using function.

def prime():
    i = 1
    while i <= 100:
	k = 0
	for j in range(1,101):
	    if i%j == 0:
		k += 1
	if k == 2:
	    print i,
	i += 1
prime()           

