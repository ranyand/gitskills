def fact(n):
	if n==1:
		return 1
	return n * fact(n - 1)
print 'please enter a number:'
x = raw_input()
xx = fact(int(x))
print xx
