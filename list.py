#!/usr/bin/python
#list.py
#python program to use all list operations.

def lst():  
    l = [1, 2, 3]
    m = ['s', 'e', 'p']
    l.append('d')
    print l
    l.pop()
    print l
    l.extend(m)
    print l
    print l.count(3)
    print l.index(2)
    l.remove(3)
    print l
    l.reverse()
    print l
    l.sort()
    print l
    l.insert(4, 'g')
lst()
