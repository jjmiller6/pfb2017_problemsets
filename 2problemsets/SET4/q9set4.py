#!/usr/bin/env python3

import sys

for i in range(int(sys.argv[1]),(int(sys.argv[2])+1),1):
	if i%2 == 1:        
		print(i)

