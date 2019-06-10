import math

def is_armstrong_number(number):
	og_number = str(number);
	n_number = 0;

	for digit in og_number:
		n_number += math.pow(int(digit), len(og_number))

	return n_number == int(og_number)

#break each number into it's digits
#raise each number to the number's length
#sum all the numbers together
#compare to original number