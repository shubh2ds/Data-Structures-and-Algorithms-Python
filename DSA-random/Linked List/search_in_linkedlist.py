#Linkedlist implementation
class Node:
    def __init__(self,key):
        self.key=key
        self.next=None

head=Node(10)
head.next=Node(20)
head.next.next=Node(30)
head.next.next.next=Node(20)
print(head)

def print_Linkedlist(head):
   curr=head
   while curr!=None:
       print(curr.key)
       curr=curr.next
print_Linkedlist(head)

def search_in_print_Linkedlist(k,head):
    curr=head
    pos=1
    while curr!=None:

        if curr.key==k:
            print("Found:",curr.key,pos)
            #break
        curr=curr.next
        pos=pos+1
    return head 
k=20
search_in_print_Linkedlist(k,head)
