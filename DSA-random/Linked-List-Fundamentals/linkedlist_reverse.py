class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self,value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
    
    def append(self, value): #else part need to be reviewed.
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next =  new_node
            self.tail =  new_node
        self.length += 1

    def prepend(self, value):
        pass

    def insert(self, index, value):
        pass
    def remove(self,index):
        pass

    def print(self):
        if self.head == None:
            print("No data")
        tmp = self.head
        while tmp is not None:
            print(tmp.value)
            tmp = tmp.next

linked_list = LinkedList(1)
linked_list.append(2)
linked_list.append(3)
linked_list.append(4)
linked_list.append(5)
linked_list.print()