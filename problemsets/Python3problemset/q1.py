#!/usr/bin/env python3
import sys
testDNA = sys.argv[1]
numberofAs = testDNA.count('A')
numberofTs = testDNA.count('T')
countoutput = "This sequence has {} As and {} Ts".format(numberofAs,numberofTs)
print(countoutput)


