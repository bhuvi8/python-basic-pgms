#!/usr/bin/env python
"""Fibonacci series
This program generates n fibonacci series numbers and prints them to the screen,
where n is given as a command line argument to the program
"""
__author__ = "Bhuvanesh Kumar (bhuvibhuvanesh@gmail.com)"
__version__ = "0.1"
__date__ = "2014-01-22 23:37"
__license__ = "WTFPL"

import sys

init1 = temp = 0
init2 = 1

try:
	input = int(sys.argv[1])
except (ValueError,IndexError):
	print ("enter a valid integer argument")
	print ("usage : "+sys.argv[0]+" <Nth fibonacci number>")
	sys.exit()

if sys.version_info > (3,):
	xrange = range

for seq in xrange(input):
	print (temp)
	init1 = init2
	init2 = temp
	temp = init1+init2
sys.exit()	
