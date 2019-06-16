def is_isogram(string):
    used_letters = []

    for char in string.lower():
    	if char.isalpha() == False:
    		pass
    	elif char in used_letters:
    		return False
    	else:
    		used_letters.append(char)

    return True
