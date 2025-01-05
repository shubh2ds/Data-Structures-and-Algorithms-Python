class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue:
    def __init__(self, value):
        new_node = Node(value)
        self.first = new_node
        self.last = new_node
        self.length = 1

    def print_queue(self):
        if self.length == 0 or self.first.value == None:
            return None
        tmp = self.first
        while tmp is not None:
            print(tmp.value)
            tmp = tmp.next

    def enqueue(self, value):
        new_node = Node(value)
        if self.length == 0 or self.first.value == None:
            self.first = new_node
            self.last = new_node
            self.length = 1
            return True
        self.last.next = new_node
        self.last = new_node
        self.length += 1
        return True
    
    def dequeue(self):
        if self.length == 0 or self.first.value == None:  
            return False
        
        self.first = self.first.next
        #tmp.next =None
        


qu = Queue(1)
qu.print_queue()
qu.enqueue(2)
qu.enqueue(3)
qu.enqueue(4)
print("enqued 1,2,3,4")
qu.print_queue()
print("dequeue.. two times")
qu.dequeue()
qu.dequeue()
qu.print_queue()
#OP: 
"""
enqued 1,2,3,4
1
2
3
4
dequeue.. two times
3
4
"""