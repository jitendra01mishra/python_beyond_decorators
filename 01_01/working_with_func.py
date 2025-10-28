def fib(n):
    '''Return the nth number in the Fibonacci sequence.'''
    if n < 2:
        return n
    else: 
        return fib(n-1) + fib(n-2)


print(fib(1))
print(fib(5))
print(fib(8))

help(fib)
