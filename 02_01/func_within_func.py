def outer(a, b, c):
    '''Accepts three arguments and uses an inner function to compute a result.'''
    def wrapper():
        '''Returns 3 fibonacci numbers a, b and c'''
        return a, b, c
    return wrapper 

#wrapper()

print(outer(5, 7, 9)())
