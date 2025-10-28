from time import perf_counter
from functools import wraps

def timer(func):
    '''Decorator that prints the execution time for the decorated function'''
    @wraps(func)
    def wrapper_timer(*args, **kwargs):
        start_time = perf_counter()    # 1
        value = func(*args, **kwargs)
        end_time = perf_counter()      # 2
        run_time = end_time - start_time    # 3
        #print(f"Duration: {run_time:.8f} seconds")
        print(f'Finished {func.__name__!r} ({args}) = {value} --> Duration {run_time:.8f} secs')
        return value
    return wrapper_timer

@timer
def fib(n):
    '''Return the nth value from the Fiboanacci sequence'''
    if n < 2:
        return n
    else:
        return fib(n-1) + fib(n-2)

fib(50)
