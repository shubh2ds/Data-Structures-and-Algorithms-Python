def merge_lists(L1,L2):
  L=L1+L2
  L.sort()
  return L
L1=[2,5,11,7,4]
L2=[12,6,1,6,33]
print(merge_lists(L1,L2))

#Time Complexity Always:
#TC: (m+n)log(m+n) 

#Space Complexity:
#require any extra memory.
#SC:O(m+n)  

#OUTPUT: [1, 2, 4, 5, 6, 6, 7, 11, 12, 33]
