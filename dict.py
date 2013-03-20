#!/usr/bin/python
#dict.py
#python program for all dictionary operations.

def dic():
    d = {'a': 1, 'b': 2, 'c': 3, 1: 9, 'sandeep': 10}
    d['d'] = 4
    print d
    d.copy()
    print d
    print d.has_key(2)
    print d.get('c')
    print d.get('f', 4)
    print d.items()
    print d.iteritems()
    print d.iterkeys()
    print d.itervalues()
    print d.keys()
    print d.pop('c')
    print d
    print d.pop('e', 5)
    print d
    print d.popitem()
    print d
    print d.setdefault(7, 6)
    print d.values()
    print d.viewitems()
    print d.viewkeys()
    print d.viewvalues()
dic()    
