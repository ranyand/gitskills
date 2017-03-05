class Fib(object):
	def __init__(self):
		self.a, self.b =0, 1 # initialize the counter a and b

	def __iter__(self):
		return self # shili benshen jiushi diedai duixiang ,so,return itself.

	def next(self):
		self.a, self.b = self.b, self.a + self.b # calculate the next value
		if self.a > 100000: # the condition to exit circulation.
			raise StopIteration();
		return self.a # return the next value
