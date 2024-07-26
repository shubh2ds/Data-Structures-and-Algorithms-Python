def isSorted(L):
    if len(L) == 0 or len(L) == 1:
        return True
    if L[0] > L[1]:
        return False
   
    
    if isSorted(L[1:]):
        return True
    else:
        return False
    
print(isSorted([11,22,3,44]))