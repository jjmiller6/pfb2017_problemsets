#!/usr/bin/env python3

readingfile = open("Python_05.txt","r")
filecontent = readingfile.read()
splitting = filecontent.split('\n')
for line in splitting:
	uppercase = line.upper()
	print(uppercase)
	

