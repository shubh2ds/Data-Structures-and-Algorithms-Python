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

def insert_in_last(k,head):
    if head==None:
        return Node(k)
    tmp=Node(k)
    curr=head
    while curr.next!=None:
        #if curr.next==None: #loop would never hit this line.
        #    curr.next=Node(k)
        curr=curr.next
        if curr.next==None: 
            curr.next=Node(k)
            return head
    #curr.next=Node(k)
    return head

def insert_in_last2(k,head):
    if head==None:
        return Node(k)
    tmp=Node(k)
    curr=head
    while curr.next!=None:
        curr=curr.next    
    curr.next=Node(k)
    return head
def insert_at_pos1(pos,data,head):
    tmp=Node(data)
    curr=head
    idx=1
    while idx+1!=pos:
        print("idx:",idx)
        curr=curr.next
        idx=idx+1
    tmp.next=curr.next   
    curr.next=tmp
    return head
def insert_at_pos2(pos,data,head):
    tmp=Node(data)
    curr=head   
    for i in range(pos-2):
        curr=curr.next
    tmp.next=curr.next
    curr.next=tmp
    return head
    
        
k=100
#new_list=insert_in_begining2(k,head)
#new_list=insert_in_last2(k,head)
pos=3
data=500
new_list=insert_at_pos2(pos,data,head)
print_Linkedlist(new_list)
