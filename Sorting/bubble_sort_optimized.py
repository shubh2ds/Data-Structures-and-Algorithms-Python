#Bubble Sort-Optimized.
#Compare adjacent and swap adjacent if L[i+1]<L[i] and move forward till the last element.Finally largest would be moved to the end, Repeat.
L=[10,8,20,5,22,3]
for j in range(0,len(L)-1):
  for i in range(len(L)-1-j):
    if L[i+1]<L[i]:
      #swap
      tmp=L[i]
      L[i]=L[i+1]
      L[i+1]=tmp
    else:
      continue
print(L)
#OUTPUT: [3, 5, 8, 10, 20, 22]
