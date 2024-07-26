def is_list_sorted_index_way(list1,idx):
  if len(list1)==0 or len(list1)==1:
    return True
  if idx==len(list1):
    return True
  if list1[idx-1]>list1[idx]:
    return False
  return is_list_sorted_index_way(list1,idx+1)

list1=[1,2,3,4,15]
idx=1
is_list_sorted_index_way(list1,idx)

