def merge_sorted(L1,L2):
  i=0
  j=0
  L_sorted=[]
  while i<len(L1) and j<len(L2):

    if L1[i]<=L2[j]:
      L_sorted.append(L1[i])
      i=i+1
    else:
      L_sorted.append(L2[j])
      j=j+1

  while i<len(L1):
    L_sorted.append(L1[i])
    i=i+1
  while j<len(L2):
    L_sorted.append(L2[j])
    j=j+1
  return L_sorted

L1=[1,7,9,10,50]
L2=[2,4,8,11,18,30,60,70,60,506]
L_sorted=merge_sorted(L1,L2)
L_sorted

#OP: [1, 2, 4, 7, 8, 9, 10, 11, 18, 30, 50, 60, 70, 60, 506]

#Time Complexity
#O(n)
