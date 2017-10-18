#!/usr/bin/env python3
import sys
testDNA = sys.argv[1]
numberofAs = testDNA.count('A')
numberofTs = testDNA.count('T')
totalnumbernucleotides = len(testDNA)
ATcontent = (numberofAs + numberofTs)/totalnumbernucleotides
GCcontent = 1 - ATcontent
countoutput = "This sequence has {:.2%} AT content and {:.2%} GC content".format(ATcontent,GCcontent)
print(countoutput)



