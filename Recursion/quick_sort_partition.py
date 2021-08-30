def partition_for_quick_sort(arr,sidx,eidx):
  pivot=arr[sidx]
  c=0
  for i in range(sidx,eidx+1):
    if arr[i]<pivot:
      c=c+1
  arr[sidx+c],arr[sidx] = arr[sidx],arr[sidx+c]
  pivot_idx=sidx+c
  i=sidx
  j=eidx
  while i<j:
    if arr[i]<pivot:
      i=i+1
    elif arr[j]>=pivot:
      j=j-1
    else:
      arr[i],arr[j]=arr[j],arr[i]
      i=i+1
      j=j-1
  return pivot_idx

arr=[6,2,1,4,3,8,9,12,5]
sidx,eidx=0,len(arr)-1
partition(arr,sidx,eidx)
print(arr)
