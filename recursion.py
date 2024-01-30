# finding factorial
def factorial(n):
    ''' gives the factorial of n
    '''
    if (n==0 or n==1):
        return 1
    else:
        return n*factorial(n-1)

print(factorial(3))
print(factorial(4))
print(factorial(5))

# finding fibonacci series
def fibonacci(n):
    ''' gives fibonacci series till n
    '''
    if (n==0):
        return 0
    elif (n==1):
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)

print(fibonacci(2))
print(fibonacci(3))
print(fibonacci(4))
print(fibonacci(5))
print(fibonacci(6))
print(fibonacci(10))





