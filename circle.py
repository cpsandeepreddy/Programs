#!/usr/bin/python
#circle.py
#python program to print circle.

def circle(h):
    k = h * ' '
    print k + '*'
    l = h - 3
    p = 1
    r = 3
    for i in range((h - 1)/2): 
	m = p * ' '
        print l * ' ' + '*' + 5 * m + '*'
	l -= 3
	p += 1
    print '*' + (h - 1) * ' ' + '*'
    for j in range((h - 1)/2):
	n = (p - 2) * ' '
	print r * ' '+ '*' + 5 * n + '*'
	r += 3
	p -= 1
    print k
circle(10)  
    
