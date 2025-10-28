def my_decorator(func):
    '''Decorator function'''
    def wrapper():
        '''Wrapper function - Return string F-I-B-O-N-A-C-C-I'''
        return 'F-I-B-O-N-A-C-C-I'
    return wrapper

@my_decorator
def pfib(n):
    '''Return Fibonacci'''
    return 

# pfib = my_decorator(pfib)
print(pfib())