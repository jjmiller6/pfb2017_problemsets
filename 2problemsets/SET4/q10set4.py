#!/usr/bin/env python3

seqlist = ['ATGCCCGGCCCGGC','GCGTGCTAGCAATACGATAAACCGG','ATATATATCGAT','ATGGGCCC']

#for seq in seqlist:
#	print(seq)

for seq in seqlist:
	print(str(len(seq))+'\t'+seq+'\n')
	print('{}{}{}{}'.format(len(seq),'\t',seq,'\n'))





