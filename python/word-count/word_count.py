import re

def count_words(sentence):
	words = re.findall(r"(?<!\\)([a-zA-Z0-9]+('[a-zA-Z0-9]+)*)", sentence.lower())	
	# returns as a list of tuples that need to be parsed out
	word_count = {}
	for word in words:
		word_count[word[0]] = words.count(word)
	
	return word_count
