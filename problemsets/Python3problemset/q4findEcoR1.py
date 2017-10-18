#!/usr/bin/env python3
import sys
DNA = sys.argv[1]
EcoR1startposition = DNA.find('GAATTC') + 1
print("EcoR1 starts at nucleotide {}".format(EcoR1startposition))

