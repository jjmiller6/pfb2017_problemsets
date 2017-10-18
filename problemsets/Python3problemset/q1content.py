#!/usr/bin/env python3
import sys
testDNA = sys.argv[1]
numberofAs = testDNA.count('A')
numberofTs = testDNA.count('T')
totalnumbernucleotides = len(testDNA)
ATcontent = (numberofAs + numberofTs)/totalnumbernucleotides
countoutput = "This sequence has {:.2%} AT content".format(ATcontent)
print(countoutput)
