class InputCell(object):
	def __init__(self, initial_value):
		self.value = initial_value


class ComputeCell(object):
	def __init__(self, inputs, compute_function):
		callback = compute_function([i.value for i in inputs])
		#print(compute_function(inputs.value))
		self.value = next(callback)

	def add_callback(self, callback):
		pass

	def remove_callback(self, callback):
		pass
