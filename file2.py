#!/usr/bin/python
#python program to open the file and write the content to it.

def files():
    fp = open('/home/sandeep/programs/file3.py','w')
    print fp.write('#this is output for file write operation.')
files()
