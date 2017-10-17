#!/usr/bin/env python3

import sys

number = float(sys.argv[1])

if number < 0:
	message = 'is negative'
	print(number, message)
elif number > 0 and number < 50 and number%2==0:
	message = 'is positive, less than 50, and even'
	print(number, message)
elif number > 0 and number > 50 and number%3==0:
	message = 'is positive, greater than 50, and divisible by 3'
	print(number, message)



