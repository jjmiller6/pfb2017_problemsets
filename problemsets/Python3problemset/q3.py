#!/usr/bin/env python3
import sys

DNA = sys.argv[1]
replacedDNA = DNA.replace('A', 't').replace('C', 'g').replace('G', 'c').replace('T', 'a')
capsreplacedDNA = replacedDNA.upper()
RevCompDNA = capsreplacedDNA[::-1]
print(RevCompDNA)
