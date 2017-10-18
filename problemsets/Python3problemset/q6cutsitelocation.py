#!/usr/bin/env python3
import sys
DNA = sys.argv[1]
startfrag1 = '1'
endfrag1 = DNA.find('GAATTC') + 1
startfrag2 = DNA.find('GAATTC') + 2
endfrag2 = len(DNA)
print("After EcoR1 cut, frag1 starts at {} and ends at {}, and frag2 starts at {} and ends at {}".format(startfrag1,endfrag1,startfrag2,endfrag2))


