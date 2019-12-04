def test_num(num):
	if test_double(num) == False:
		return False
	if test_not_desc(num) == False:
		return False
	return True


def test_double(num):
	char = str(num)
	is_two = False
	count = 0
	c = 'a'
	
	for x in range(0,len(char)):
		if char[x] == c:
			count += 1 
		if char[x] != c:
			if count == 2:
				return True
			count = 1
		c = char[x]
	
	if count == 2 or is_two == True:
		return True
		
	return False

def test_not_desc(num):
	char = str(num)
	for x in range(0,len(char)-1):
		if char[x] > char[x+1]:
			return False
	return True

def test_range():
	count = 0 
	for i in range(137683, 596254):
		if test_num(i) == True:
			count += 1
			print(count)
	return count
			
print( test_range() )