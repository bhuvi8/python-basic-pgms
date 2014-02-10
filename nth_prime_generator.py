#!/usr/bin/env python
"""Prime Num Generator
This program finds the nth prime number, where n is input to 
the program as a command line argument.
"""
__author__ = "Bhuvanesh Kumar (bhuvibhuvanesh@gmail.com)"
__version__ = "0.2"
__date__ = "2014-02-07"
__license__ = "WTFPL"

import sys

try:
	n = int(sys.argv[1])
except (ValueError,IndexError):
	print ("input a valid integer argument")
	print ("usage : "+sys.argv[0]+" <Nth prime number>")
	sys.exit()

if sys.version_info > (3,):
	xrange = range


if (n <= 0):
	print("input a positive integer")
	sys.exit()
elif (n == 1):
	print("%d" %2)
	sys.exit()
	

candidate = 3
while(1):
	if (candidate % 2 != 0):
		for factor in xrange(3,(candidate//3)+1,2):
			if (candidate % factor == 0):
				break
		else:
			n-=1
		if(n<=1):
			print (candidate)
			break
	candidate+=2
sys.exit()
