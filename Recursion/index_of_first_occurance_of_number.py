def firstIndex(arr, x, n):
    # Please add your code here
    
    if len(arr)==0:
        return -1
    if arr[0]==x:
        return n-len(arr) #len ( original array) - len(current sliced array)
    
    return firstIndex(arr[1:], x, n)

# Main
from sys import setrecursionlimit
setrecursionlimit(11000)
n=int(input())
arr=list(int(i) for i in input().strip().split(' '))
x=int(input())
print(firstIndex(arr, x, n))
