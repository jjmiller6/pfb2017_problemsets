#!/usr/bin/env python3
import sys

DNA = sys.argv[1]
startfrag1 = 0
endfrag1 = DNA.find('GAATTC') + 1
Frag1 = DNA[startfrag1:endfrag1]
startfrag2 = DNA.find('GAATTC') + 1
endfrag2 = len(DNA)
Frag2 = DNA[startfrag2:endfrag2]
lengthfrag1 = len(Frag1)
lengthfrag2 = len(Frag2)
print("{}\t{}\t{}".format(Frag1, startfrag1, lengthfrag1))
print("{}\t{}\t{}".format(Frag2, startfrag2, lengthfrag2))







