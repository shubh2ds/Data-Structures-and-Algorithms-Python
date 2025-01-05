def factorial_of_n(n):
    if n==1:
        return n
    return n*factorial_of_n(n-1)
n=4
factorial_of_n(n)       
