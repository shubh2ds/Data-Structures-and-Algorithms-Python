#Linkedlist implementation
class Node:
    def __init__(self,key):
        self.key=key
        self.next=None

head=Node(10)
head.next=Node(20)
head.next.next=Node(30)
head.next.next.next=Node(40)
#print(head)

def print_Linkedlist(head):
   curr=head
   while curr!=None:
       print(curr.key)
       curr=curr.next

def sorted_insert(k,head):
    tmp=Node(k)
    if head is None:
        return None
    elif head.key>k:
        tmp.next=head
        return tmp
    else:
        curr=head
        while curr.next !=None and curr.next.key<k:
            curr=curr.next
        tmp.next=curr.next
        curr.next=tmp
        return head
    

k=11
new_list=sorted_insert(k,head)

print_Linkedlist(new_list)
