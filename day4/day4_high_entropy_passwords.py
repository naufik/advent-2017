'''
	Advent of Code - Day 4
	High Entropy Passphrases

	High-Level Solution by Naufal Fikri
	http://github.com/naufik
'''

def all_words_unique(sentence):
	''' Checks whether all the words in a given passphrase is unique or not'''
	return len(sentence.split(" ")) == len(set(sentence.split(" ")))

def count_valid_lines(filename):
	''' Checks how many lines in a given filename are valid passphrases'''
	finput = open(filename, "r")
	flines = []
	for line in finput:
		flines.append(line[:-1])
	return len([i for i in flines if all_words_unique(i)])

#run my given input, our input files might be different.
print(count_valid_lines("testcase"))