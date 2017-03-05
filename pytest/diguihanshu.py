def fact(n):
	return fact_iter(n,1)

def fact_iter(num,product):
	if num==1:
		return product
	return fact_iter(num - 1, num * product)
print 'please enter a number:'
x = raw_input()
xx = fact(int(x))
print xx
