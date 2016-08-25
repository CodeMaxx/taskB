from complexno import *

def myexponent(x):
	val = 1
	term = 1
	for i in range(1,6):
		term = x*term/i 
		val = term + val
	return val