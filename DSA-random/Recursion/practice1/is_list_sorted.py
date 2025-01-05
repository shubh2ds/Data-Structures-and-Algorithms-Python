def is_list_sorted(list1):
  if len(list1)==0 or len(list1)==1:
    return True
  if list1[0]>list1[1]:
    return False
  return is_list_sorted(list1[1:])
list1=[1,2,3,4,15]
is_list_sorted(list1)
