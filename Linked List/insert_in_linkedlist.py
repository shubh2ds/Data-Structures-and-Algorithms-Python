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
#print_Linkedlist(head)

def insert_in_begining(k,head):
    if head is None:
        head=Node(k)
        return head
    tmp=head
    head=Node(k)
    head.next=tmp
    return head
k=100
head=insert_in_begining(k,head)
print_Linkedlist(head)
