#take 1st minm element put it on the 1st place.
#take 2nd minm element put it on the 2nd place.
#take nth minm element put it on the nth place.
def get_min(L):
  min=L[0]
  i=0
  idx=i
  while(i<len(L)):
    if L[i]<min:
      min=L[i]
      idx=i
    i=i+1
  return min,idx
#L=[12,13,54,4,4,7]
min,idx=get_min(L)

def selection_sort(L):
  for i in range(0,len(L)-1):
    print(L[i:])
    minm,min_idx=get_min(L[i:]) #min(L[i:])  
    min_idx=min_idx+i
    print("minm,min_idx:",minm,min_idx)
    if L[i]>minm:
      tmp=L[i]
      L[i]=minm
      L[min_idx]=tmp
      print("Swapped:",L)
  return L

L=[3,1,6,2,6,20,7,7,10]   
L_sorted=selection_sort(L)  
print(L_sorted)

#Time Complexity Always:
#TC: O(n2) 

#Space Complexity:
#Does not require any extra memory.
#SC:O(1)  

#It is not the Stable algorithm: Order of the duplicate elements may not be same after sorting.

#OUTPUT:[1, 2, 3, 6, 6, 7, 7, 10, 20]
