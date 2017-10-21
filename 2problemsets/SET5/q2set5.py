#!/usr/bin/env python3

input = open("Python_05.txt","r")
output = open("Python_05_uc.txt","w")

contents = input.read()

#splitlist = contents.split('\n') why no longer need to split?

for item in contents:
        output.write(item.upper())

input.close()
output.close()
print("Wrote 'Python_05_uc.txt'")

