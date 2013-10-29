from nltk.tokenize import RegexpTokenizer
from collections import Counter

infile = open('names.txt', 'r')
names = infile.read()

tokenizer = RegexpTokenizer(r'\w+')
# tokens = tokenizer.tokenize(names)
tokens = tokenizer.tokenize(names)

tokens.sort()

total = 0
count = 1

# setup the value dictionary
values = dict()

for x in xrange(0,26):
	values[chr(ord('A') + x)] = x + 1

for word in tokens:
	thisRun = 0
	for x in word:
		thisRun = thisRun + values[x]
	thisRun = thisRun * count
	print word, thisRun
	total = total + thisRun
	count = count + 1

print total

# for word in tokens:
# 	print word

# print filter(lambda word: word not in ',-', tokens)
