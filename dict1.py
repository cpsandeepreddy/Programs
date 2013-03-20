#!/usr/bin/python
#dict1.py
#python program for getting dictionary from two lists.

l1 = [1, 2, 3, 4]
l2 = [5, 6, 7, 8, 9]
d = {}
for i in range(len(l1)):
    d[l1[i]] = l2[i]
print d

      
