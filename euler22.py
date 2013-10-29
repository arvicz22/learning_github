from nltk.tokenize import RegexpTokenizer
from collections import Counter

# Opens the file and reads it in
infile = open('names.txt', 'r')
names = infile.read()

#regex it to death
tokenizer = RegexpTokenizer(r'\w+')
tokens = tokenizer.tokenize(names)
tokens.sort()

# setup the value dictionary
values = dict()
for x in xrange(ord('A'), ord('Z') + 1):
	values[chr(x)] = x - ord('A') + 1

#points
total = 0
for idx, word in enumerate(tokens, start=1):
	thisName = 0
	for x in word:
		thisName = thisName + values[x]
	thisName = thisName * idx
	total = total + thisName

print 'The total score is', total
