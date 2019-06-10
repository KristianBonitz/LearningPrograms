import string
import random

class Robot(object):
	def __init__(self):
		self.name = create_name()

	def reset(self):
		new_name = create_name()
		while new_name == self.name:
			new_name = create_name()

		self.name = new_name


def create_name():
	name = ""
	name += random.choice(string.ascii_uppercase) 
	name += random.choice(string.ascii_uppercase)
	name += random.choice(string.digits)
	name += random.choice(string.digits)
	name += random.choice(string.digits)
	return name



# Generate Name
# Check name against other names 
# (repeat)
