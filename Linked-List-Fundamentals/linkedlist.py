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

    def append(self,value):
        pass

    def prepend(self,value):
        pass

    def insert(self,index,value):
        pass
    def print(self):
        if self.head == None:
            return None
        tmp = self.head
        while tmp is not None:
            print(tmp.value)
            tmp = tmp.next


linked_list = LinkedList(4)
#linked_list = LinkedList(5)
linked_list.print()