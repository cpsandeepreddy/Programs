#!/usr/bin/python
#numbers.py
#python program to print number in words using tuples.

def number(k):
    l = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    m = ['eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
    n = ['ten', 'twenty', 'thirty', 'fourty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
    if k < 10:
        print l[k - 1]
    elif k >= 11 and k < 20:
        p = k%10
        print m[p - 1]
    elif k > 20:
        i = k/10 
        j = k%10
        if i > 0 and j > 0:
            print n[i - 1] + ' ' + l[j - 1]
        elif i > 0 and j == 0:
            print n[i - 1]
    else:
	print n[0]
number(49) 
