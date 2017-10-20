#!/usr/bin/env python3

mylist = [101,2,15,22,95,33,2,27,72,15,52]

mylist.sort() #does this change mylist? why no assign it? not needed with this

print(mylist)

sumeven = 0
sumodd = 0


for num in mylist:
	if num % 2 == 0:
		sumeven = sumeven + num
	if num % 2 == 1:
		sumodd = sumodd + num

print(sumeven)
print(sumodd)
