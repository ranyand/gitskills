class Student(object):

	def __init__(self, name, score):
		self.name = name
		self.score =score

	def print_score(self):
		print '%s: %s' % (self.__name,self.__score)

	def get_name(self):
		return self.__name

	def get_score(self):
		return self.__score

	def set_score(slef,score):
		if 0 <= score <=100:
			self.__score = score
	else:
			return ValueError('bad score') #when rasie syntaxerror:invalid syntax

	def get_grade(self,score):
		if self.score>=90:
			return 'A'
		elif self.score>=60:
			return 'B'
		else:
			return 'C'
