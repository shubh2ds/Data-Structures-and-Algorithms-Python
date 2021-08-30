#To complete
def firstIndex(arr, x,idx):
   if len(arr)==0 or idx==len(arr):
     return -1
   if arr[idx]==x:
     return idx
   return firstIndex(arr, x,idx+1)

# Main
from sys import setrecursionlimit
setrecursionlimit(11000)
n=int(input())
arr=list(int(i) for i in input().strip().split(' '))
x=int(input())
idx=0
print(firstIndex(arr, x, idx))
