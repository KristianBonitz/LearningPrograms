def score(word):
	score = 0
	for letter in word.upper():
		if letter in ['A', 'E', 'I', 'O', 'U', 'L', 'N', 'R', 'S', 'T']:
			score += 1
		elif letter in ['D', 'G']:
			score += 2
		elif letter in ['B', 'C', 'M', 'P']:
			score += 3
		elif letter in ['F', 'H', 'V', 'W', 'Y']:
			score += 4
		elif letter in ['K']:
			score += 5
		elif letter in ['J', 'X']:
			score += 8
		elif letter in ['Z', 'Q']:
			score += 10

	return score