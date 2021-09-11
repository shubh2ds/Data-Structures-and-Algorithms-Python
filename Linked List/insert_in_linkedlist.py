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

def insert_in_begining1(k,head):
    if head is None:
        head=Node(k)
        return head
    tmp=head
    head=Node(k)
    head.next=tmp
    return head
def insert_in_begining2(k,head):
    tmp=Node(k)
    tmp.next=head
    return tmp
k=100
new_list=insert_in_begining2(k,head)

print_Linkedlist(new_list)
