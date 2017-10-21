#!/usr/bin/env python3

file = open("Python_05.txt","r")

contents = file.read()

#print(contents)

splitlist = contents.split('\n') #split outputs as a list, also gets rid of what you split on

#print(splitlist)

for item in splitlist:
	print(item.upper())

