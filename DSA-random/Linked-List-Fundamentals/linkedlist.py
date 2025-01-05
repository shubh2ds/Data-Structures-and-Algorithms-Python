class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self,value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def append1(self,value):
        if self.head == None:
            return Node(value)
        tmp = self.head
        while tmp.next is not None:
            tmp = tmp.next
        tmp.next = Node(value)
        #return tmp
        #pass

    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def prepend(self,value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            tmp = self.head
            self.head = new_node
            new_node.next = tmp
        self.length += 1

    def pop_first(self):
        if self.length == 0 :
            return None
        else:
            tmp = self.head
            self.head = self.head.next
            tmp.next = None
            self.length -= 1
            if self.length == 0:
                self.tail = None
            return tmp.value
        
    def pop(self):
        if self.length == 0 :
            return False
        if self.length == 1 :
            self.head = None
            self.tail = None
            self.length = 0
            return True
        tmp = self.head
        for _ in range(self.length-1):
            tmp = tmp.next
        tmp.next = None
        tmp = None

        self.length -= 1
        return True
        
    def get(self,index):
        if index<0 or index >= self.length:
            return None 
        tmp = self.head 
        for _ in range(0,index):
            tmp = tmp.next
        return tmp.value
    
    def set(self,index,value):
        if index<0 or index >= self.length:
            return False
        tmp = self.head
        for _ in range(index):
            tmp = tmp.next
        tmp.value = value
        return True

    def insert(self,index,value):
        if index < 0 or index >= self.length:
            return False
        if index == 0:
            self.prepend(value)
        if index == self.length:
            self.append(value)
        tmp = self.head
        for _ in range(index-1):
            tmp = tmp.next
        new_node= Node(value)
        new_node.next = tmp.next
        tmp.next = new_node
        return True
    
    def remove(self,index):
        if index < 0 or index >= self.length:
            return False
        if index == 0:
            self.pop_first()   
        if index == self.length:
            self.pop()
        tmp = self.head
        for _ in range(index-1):
            tmp = tmp.next
        tmp.next = tmp.next.next
        return True

    def print(self):
        if self.head == None:
            return None
        tmp = self.head
        while tmp is not None:
            print(tmp.value)
            tmp = tmp.next

linked_list = LinkedList(4)
#linked_list = LinkedList(5)
linked_list.append(5)
linked_list.append(6)
linked_list.append(7)
linked_list.print()
print("after prepend")
linked_list.prepend(70)
linked_list.prepend(60)
linked_list.prepend(50)
linked_list.print()
print("pop first")
print(linked_list.pop_first())
print("after pop")
linked_list.print()
print("get at 3:", linked_list.get(3))
linked_list.set(3,100)
print("get after set of 100 at 3:", linked_list.get(3))
print("insert 1000 at 3rd index.")
linked_list.insert(3,1000)
linked_list.print()
print("pop:",linked_list.pop())
#print("pop:",linked_list.pop())
linked_list.print()
print("remove:",linked_list.remove(3))
linked_list.print()