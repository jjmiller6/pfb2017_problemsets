#!usr/bin/env python3

fastafile = open("Python_05.fasta","r")

#rfastafile = fastafile.read() is this necessary?

for line in fastafile:
	line = line.strip()
	if line.startswith(">"):
		if seq!= '':
			#actionline
			print(header, seq)
			seq = ''
		header = line
	else:
		seq+= line
#actionline
print(header, seq)
