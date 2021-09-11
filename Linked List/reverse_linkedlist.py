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
       
def reverse(head):
    if head is None:
        return None

    curr=head
    stack=[]
    while curr is not None:
        stack.append(curr.key)
        curr=curr.next
    curr=head
    while curr is not None:
        curr.key=stack.pop()
        curr=curr.next
    return head
new_list=reverse(head)

print_Linkedlist(new_list)
