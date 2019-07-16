class InputCell(object):
	def __init__(self, initial_value):
		self.value = initial_value


# requires some update system to be implemented
class ComputeCell(object):
	def __init__(self, inputs, compute_function):
		self.function = compute_function
		self.inputs = inputs

	def add_callback(self, callback):
		pass

	def remove_callback(self, callback):
		pass

	@property
	def value(self):
		return self.function([i.value for i in self.inputs])
