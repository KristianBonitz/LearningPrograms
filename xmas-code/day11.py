class Robot(object):
	"""docstring for Robot"""
	def __init__(self):
		super(Robot, self).__init__()
		self.orientations = ['Up', 'Right', 'Down', 'Left']
		self.dir = 0
		self.x = 0
		self.y = 0

	def move(self, action):
		if self.orientations[self.dir] == 'Up':
			self.x += (1 if action == 0 else -1)
		elif self.orientations[self.dir] == 'Right':
			self.y += (1 if action == 0 else -1)
		elif self.orientations[self.dir] == 'Down':
			self.x += (-1 if action == 0 else 1)
		elif self.orientations[self.dir] == 'Left':
			self.y += (-1 if action == 0 else 1)

		self.dir = (self.dir + 1 if action == 0 else self.dir - 1) % len(self.orientations)

		return self.x, self.y

	def run_actions(self, action_list):
		positions = [(self.x, self.y)]

		for a in action_list:
			pos = self.move(a)

			if pos not in positions:
				positions.append(pos)

		print(positions, len(positions))

	def print(self):
		print(self.x, self.y, self.orientations[self.dir])

# Test commands = [0,0 ,1,0 ,1,0, 1,0, 0,1, 1,0, 1,0]
commands = [1,1,0,0,1,1,0,0,1,1,0,0,1,1,0,0,1,1,0,0,1,1,0,0,1,1,0,0,1,1,0,0,1,1,0,0,1,1,0,0,1,1,0,0,1,1,0,0,1,1,0,0,1,1,0,0,1,1,0,0,1,1,0,0,1,1,0,0,1,1,0,0,1,1,0,0,1,1,0,0,1,1,0,1,1,0,1,1,0,0,1,1,0,0,1,1,0,0,1,1,0,0,1,1,0,0,1,1,0,0,1,1,0,0,1,1,0,0,1,1,0,0,1,1,0,0,1,1,0,0,1,1,0,0,1,1,0,0,1,1,0,0,1,1,0,0,1,1,0,0,1,1,0,0,1,1,0,0,1,1,0,0,1,1,0,0,1,0,0,1,0,0,1,1,0,0,1,1,0,0,1,1,0,0,1,1,0,0,1,1,0,0,1,1,0,0,1,1,0,0,1,1,0,0,1,1,0,0,1,1,0,0,1,1,0,0,1,1,0,0,1,1,0,0,1,1,0,0,1,1,0,0,1,1,0,0,1,1,0,0,1,1,0,0,1,1,0,0,1]

rob = Robot()
rob.run_actions(commands[1::2])