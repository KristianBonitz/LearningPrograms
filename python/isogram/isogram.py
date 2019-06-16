def is_isogram(string):
    for char in string.lower():
    	if char.isalpha() and string.lower().count(char) > 1:
    		return False

    return True
