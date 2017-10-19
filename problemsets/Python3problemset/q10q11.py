>>> sorted(gene, key=len)
['GATGGGATTGGGGTTTTCCCCTCCCATGTGCTCAAGACTGGCGCTAAAAGTTTTGAGCTTCTCAAAAGTCTAGAGCCACCGTCCAGGGAGCAGGTAGCTGCTGGGCTCCGGGGACACTTTGCGTTCGGGCTGGGAGCGTGCTTTCCACGACGGTGACACGCTTCCCTGGATTGGCAGCCAGACTGCCTTCCGGGTCACTGCCATGGAGGAGCCGCAGTCAGATCCTAGCGTCGAGCCCCCTCTGAGTCAGGAAACATTTTCAGACCTATGGAAACTACTTCCTGAAAACAACGTTCTGTCCCCCTTGCCGTCCCAAGCAATGGATGATTTGATGCTGTCCCCGGACGATATTGAACAATGGTTCACTGAAGACCCAGGTCCAGATGAAGCTCCCAG', 'AATTCGCCAGAGGCTGCTCCCCCCGTGGCCCCTGCACCAGCAGCTCCTACACCGGCGGCCCCTGCACCAGCCCCCTCCTGGCCCCTGTCATCTTCTGTCCCTTCCCAGAAAACCTACCAGGGCAGCTACGGTTTCCGTCTGGGCTTCTTGCATTCTGGGACAGCCAAGTCTGTGACTTGCACGTACTCCCCTGCCCTCAACAAGATGTTTTGCCAACTGGCCAAGACCTGCCCTGTGCAGCTGTGGGTTGATTCCACACCCCCGCCCGGCACCCGCGTCCGCGCCATGGCCATCTACAAGCAGTCACAGCACATGACGGAGGTTGTGAGGCGCTGCCCCCACCATGAGCGCTGCTCAGATAGCGATGGTCTGGCCCCTCCTCAGCATCTTATCCGAGTGGAAGGAAATTTGCGTGTGGAGTATTTGGATGACAGAAACACTTTTCG']
>>> 
>>> 
>>> 
>>> 
>>> my_list = ['a', 'bb', 'ccc']
>>> list_copy = my_list
>>> my_list
['a', 'bb', 'ccc']
>>> list_copy
['a', 'bb', 'ccc']
>>> jim_list
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'jim_list' is not defined
>>> jim_list = my_list
>>> jim_list
['a', 'bb', 'ccc']
>>> 
>>> 
>>> 
>>> my_list
['a', 'bb', 'ccc']
>>> mil_list
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'mil_list' is not defined
>>> mil_copy = my_list.copy()
>>> mil_list
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'mil_list' is not defined
>>> mil_list = my_list.copy()
>>> mil_list
['a', 'bb', 'ccc']
>>> my_list
['a', 'bb', 'ccc']
>>> my_list + 'dddd'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: can only concatenate list (not "str") to list
>>> my_list + ['dddd']
['a', 'bb', 'ccc', 'dddd']
>>> mil_list
['a', 'bb', 'ccc']
>>> my_list
['a', 'bb', 'ccc']
>>> new_list = my_list + ['dddd']
>>> my_list
['a', 'bb', 'ccc']
>>> new_list
['a', 'bb', 'ccc', 'dddd']
