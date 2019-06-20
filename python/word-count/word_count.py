def count_words(sentence):
	#format sentence to remove non-words and seperate words

    words = sentence.split(' ')
    word_count = {}
    #count the number of words in sentence
    for word in words:
    	word_count[word] = sentence.count(word)
    
    return word_count
