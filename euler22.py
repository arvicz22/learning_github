from nltk.tokenize import RegexpTokenizer

infile = open('names.txt', 'r')
names = infile.read()

tokenizer = RegexpTokenizer(r'\w+')
# tokens = tokenizer.tokenize(names)
tokens = tokenizer.tokenize("()asdf asdsd asda asda!")

for word in tokens:
	print word

# print filter(lambda word: word not in ',-', tokens)
