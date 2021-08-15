#Bubble Sort
#Compare adjacent and swap adjacent if L[i+1]<L[i] and move forward till the last element.Finally largest would be moved to the end, Repeat.

def bubble_sort(L):
  for j in range(0,len(L)-1):
    Swapped=False
    for i in range(len(L)-1-j):
      if L[i+1]<L[i]:
        #swap
        tmp=L[i]
        L[i]=L[i+1]
        L[i+1]=tmp
        Swapped=True
    if Swapped==False:
      return L
  return L

L=[3,15,12,6,20,30]   
L_sorted=bubble_sort(L)  
print(L_sorted)

#Worst case :if list is unsorted.
#TC: O(n2) 

#Best case :if list is sorted.
#TC:O(n) 

#It is a Stable algorithm: Bubble sort keeps the order of the duplicate elements same after sorting.

#OUTPUT:[3, 6, 12, 15, 20, 30]
