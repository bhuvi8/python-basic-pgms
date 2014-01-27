"""twin_primes.py
This program prints a list of twin primes in a given range
If only one integer is entered, twin primes from 2 to the entered integer is
found. If no integer or an invalid input is entered, this program quits
displaying an error message.

This program is written to be compatible with both Python2+ and Python3+
"""
__autor__ = "Bhuvanesh Kumar (bhuvibhuvanesh@gmail.com)"
__version__ = "0.1"
__date__ = "2014-01-27"
__license__ = "WTFPL"

import sys

try:
	start_n = int(sys.argv[1])
except (ValueError,IndexError):
	print ("enter a numeric range in which to find twin primes")
	print ("usage: "+sys.argv[0]+" [start] <end>")
	sys.exit()
	
try:
	end_n = int(sys.argv[2])
except IndexError:
	end_n = start_n
	start_n = 2
except ValueError:
	print ("enter a numeric range in which to find twin primes")
	print ("usage: "+sys.argv[0]+" [start] <end>")
	sys.exit()

	
"""this function finds the twin primes between given ranges
arguments start and end are mandatory
this function doesnot return a value
"""
def find_twin_primes(start, end):
	#if python 3+ is used, use range instead of xrange
	if sys.version_info > (3,):
		xrange = range

	#check whether start and end both are positive integers
	if (start <= 0 or end <= 0):
		print ("enter +ve integers > 0 for both start and end of range")
		return None
	elif (start >= end):
		print ("end of range should be greater than start of range")
		return None
	elif (start <= 2):
		#if start of range is less than 3,then set 2 as frst prime
		#and start looking for primes greater than 2
		#p1 = 2
		start = 3
	elif (start % 2 == 0):
		#if start is even increment it by one, since there can be no
		#even prime other than 2
		start += 1
	p1 = 2

	#start looking for primes in the range by successive division
	for candidate in range(start,end+1,2):
		for factor in range(3,candidate//2,2):
			if (candidate % factor == 0):
				break
		else:
			#if the difference between last two primes is <= 2,
			#then display those primes as twin prime
			if (candidate - p1 <= 2):
				print ('%d %d' %(p1,candidate))
			p1 = candidate

find_twin_primes(start_n,end_n)
sys.exit()