def power(x,n=2):
	s = 1
	while n>0:
		n = n-1
		s = s*x
	return s
print 'please enter a number to c a ^:'
x = raw_input()
xx = power(int(x))
print xx
