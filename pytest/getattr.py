class Student(object):

	def __init__(self):
		self.name = 'ranyan'

	def __getattr__(self, attr):
		if attr=='score':
			return 99
