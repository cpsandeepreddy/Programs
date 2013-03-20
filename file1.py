#!/usr/bin/python
# to show examples of files.
#python  program to open the file and read the contents in it.

def files():
    fp = open('/home/sandeep/programs/file1.py', 'r+')
    print fp.read()
files()
