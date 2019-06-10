def is_isogram(string):
	for char_a in string:
		for char_b in string:
			if char_a == char_b:
				return False
	return True