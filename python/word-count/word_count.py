import re

def count_words(sentence):
	#format sentence to remove non-words and seperate words
	words = re.findall(r"(?<!\\)[a-z0-9]+", sentence.lower())
	print(words)
	#words = sentence.lower().split(r' ')
	#count the number of words in sentence
	word_count = {}
	for word in words:
		word_count[word] = words.count(word)
	
	return word_count
