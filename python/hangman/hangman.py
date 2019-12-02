# Game status categories
# Change the values as you see fit
STATUS_WIN = "win"
STATUS_LOSE = "lose"
STATUS_ONGOING = "ongoing"


class Hangman(object):
	def __init__(self, word):
		self.remaining_guesses = 9
		self.status = STATUS_ONGOING
		self.answer = word
		self.reveal_list = [False] * len(word)
		self.guesses = []
		#for length of word, create list of same length
		#e.g. 'Foo' = [False, False, False]


	def guess(self, char):
		#provide back if char in word
		#return current status of word
		#loop to check each char
		if self.status != STATUS_ONGOING:
			raise ValueError("Game has ended")

		if char in self.answer and char not in self.guesses:
			pos = 0
			for c in self.answer:
				if c == char:
					self.reveal_list[pos] = True
				pos += 1
		else: 
			self.remaining_guesses -= 1

		self.guesses.append(char)

		#check game end
		if False not in self.reveal_list:
			self.status = STATUS_WIN
		elif self.remaining_guesses < 0:
			self.status = STATUS_LOSE
		
		return

	def get_masked_word(self):
		#return word with _ where letters unknown
		pos = 0
		masked_word = ''
		while pos < len(self.answer):
			if self.reveal_list[pos] == True:
				masked_word += self.answer[pos]
			else:
				masked_word += '_'
			pos += 1

		return masked_word

	def get_status(self):
		return self.status