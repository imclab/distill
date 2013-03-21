# Python DW Clustering Utils
#
# Creator: Anant Bhardwaj


import re, random


def median(x):
	 return sorted(x)[len(x)/2]

def get_type(p):
	if type(p) is int:
		return 'i'
	if type(p) is float:
		return 'f'
	if type(p) is str:
		return 's'

def get_val(s):
	try:
		ret = int(s)
		return ret
	except ValueError:
		try:
			ret = float(s)
			return ret
		except ValueError:
			return s


def get_signature(line):
	tokens = re.split('\W+', line)
	tokens = filter(lambda x: x!='', tokens)
	signature=[get_type(get_val(token)) for token in tokens] 
	return signature
	
	
def get_signatures(f):
	data = open(f, 'rU').read()
	lines = re.split('\n',data);
	lines = filter(lambda x: x!='\n' and x!='', lines)	
	
	signatures=[]
	for line in lines:
		tokens = re.split('\W+', line)
		tokens = filter(lambda x: x!='', tokens)
		signature=[get_type(get_val(token)) for token in tokens] 
		signatures.append(signature)
	return signatures;
	

def levenshtein(s1, s2):
    if len(s1) < len(s2):
        return levenshtein(s2, s1)
    if not s1:
        return len(s2)
 
    previous_row = xrange(len(s2) + 1)
    for i, c1 in enumerate(s1):
        current_row = [i + 1]
        for j, c2 in enumerate(s2):
            insertions = previous_row[j + 1] + 1 # j+1 instead of j since previous_row and current_row are one character longer
            deletions = current_row[j] + 1       # than s2
            substitutions = previous_row[j] + (c1 != c2)
            current_row.append(min(insertions, deletions, substitutions))
        previous_row = current_row
 
    return previous_row[-1]


    

