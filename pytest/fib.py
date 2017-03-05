def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a , b=b, a + b
        n = n + 1
:browse so
for xx in fib(6): 
        print xx
