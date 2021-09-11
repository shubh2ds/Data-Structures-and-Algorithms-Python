#Linkedlist implementation
class Node:
    def __init__(self,key):
        self.key=key
        self.next=None

head=Node(10)
head.next=Node(20)
head.next.next=Node(30)
head.next.next.next=Node(20)
#print(head)

def print_Linkedlist(head):
   curr=head
   while curr!=None:
       print(curr.key)
       curr=curr.next

def delete_first(head):
    if head.next is None:
        return None
    head=head.next
    return head
def delete_last(head):
    if head is None or head.next is None:
        return None
    curr=head
    while curr.next.next is not None:
        curr=curr.next
    curr.next=None
    return head
#new_list=delete_first(head)
new_list=delete_last(head)

print_Linkedlist(new_list)
