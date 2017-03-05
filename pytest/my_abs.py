def my_abs(x):
	if not isinstance(x,(int,float)):
		raise TypeError('bad operand type')
	if x >=0:
		return x
	else:
		return -x

print 'please enter a number:'
x = raw_input() # x is a str
xx = my_abs(int(x)) #xx is a str too.and not xx is a multiplication

print xx
