def convert(number):

	response  = ''
	response += 'Pling' if number % 3 == 0 else '' 
	response += 'Plang' if number % 5 == 0 else ''
	response += 'Plong' if number % 7 == 0 else ''

	return str(number) if response == '' else response