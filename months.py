#!/usr/bin/python
#months.py
#python program to print months for tuple example.

def months(i):
    ls = ('jan', 'feb', 'mar', 'apr', 'may', 'jun',' jul', 'aug','sep', 'oct', 'nov', 'dec')
    print ls[i-1],
months(i=int(raw_input('please enter month number:')))
