def fib(n):
    if n==0 or n==1:
        return 1
    return fib(n-1)+fib(n-2)

import sys
sys.setrecursionlimit(3000)

print(fib(4)) #1,1,2,3,5,8