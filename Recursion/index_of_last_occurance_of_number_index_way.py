## Read input as specified in the question.
## Print output as specified in the question.
def lastIndex(arr, x):
    # Please add your code here
    
    if len(arr)==0 :
        return -1
    if arr[len(arr)-1]==x:
        return len(arr)-1 #len(current sliced array) -1
    
    return lastIndex(arr[0:len(arr)-1], x)

def lastIndex_index_way(arr, x, idx):
    # Please add your code here
    
    if len(arr)==0 or idx== -1:
        return -1
    if arr[idx]==x:
        return idx #len(current sliced array) -1
    
    return lastIndex_index_way(arr, x,idx-1)

# Main
from sys import setrecursionlimit
setrecursionlimit(11000)
n=int(input())
arr=list(int(i) for i in input().strip().split(' '))
x=int(input())
idx=len(arr)-1
print(lastIndex(arr, x))
print(lastIndex_index_way(arr, x,idx))
