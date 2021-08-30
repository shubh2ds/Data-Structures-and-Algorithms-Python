def checkNumber(arr, x):
    # Please add your code here
    #print(arr[0])
    if len(arr)==0:
        return False

    if arr[0]==x:
        return True
    
    arr1=arr[1:]
    return checkNumber(arr1, x)

from sys import setrecursionlimit
setrecursionlimit(11000)
n=int(input())
arr=list(int(i) for i in input().strip().split(' '))
x=int(input())
if checkNumber(arr, x):
    print('true')
else:
    print('false')
