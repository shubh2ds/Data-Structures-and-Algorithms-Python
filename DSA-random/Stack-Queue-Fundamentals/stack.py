class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self, value):
        new_node = Node(value)
        self.top = new_node
        self.height = 1
    def print_stack(self):
        if self.height <= 0:
            return "Stack is empty!"
        tmp = self.top
        while tmp is not None:
            print(tmp.value)
            tmp = tmp.next
        return "Done: total in stack:"+str(self.height)
    
    def push(self, value):
        new_node = Node(value)
        if self.height == 0 or self.top.value == None:
            self.top = new_node

            return True
        
        tmp = self.top
        self.top = new_node
        new_node.next = tmp
        self.height += 1
        return True
        
    def pop(self):
        if self.height == 0 or self.top.value == None:
            print("stack is empty!")
            return False
        tmp = self.top
        self.top = self.top.next
        tmp.next = None
        self.height -= 1
        return tmp.value

stack = Stack(None)
print("Stack defined with None value")
stack.push(1)
stack.push(2)
stack.push(3)
print("pushed 1,2,3")
stack.print_stack()
print("pop:",stack.pop())
stack.print_stack()
print("pop:",stack.pop())
stack.print_stack()
print("pop:",stack.pop())
stack.print_stack()
#===
print("pop:",stack.pop())
stack.print_stack()


#OP:
"""
Stack defined with None value
pushed 1,2,3
3
2
1
pop: 3
2
1
pop: 2
1
pop: 1
stack is empty!
pop: False
"""