#!/usr/bin/python
#month1.py
#python program to print month number of year using dictionary.

def month(n):
    d = {1:'jan',2:'feb',3:'mar',4:'apr',5:'may',6:'jun',7:'jul',8:'aug',9:'sep',10:'oct',11:'nov',12:'dec'}
    print d[n]
month(n=int(raw_input('please enter number:'))) 
