#!/usr/bin/python
#deep_copy.py
#python example program to describe deep copy.

from copy import deepcopy
l1 = ['a','b',['c','d']]
l2 = deepcopy(l1)
l2[1] = 'e'
l2[2][1] = 'f'
print l1
print l2
