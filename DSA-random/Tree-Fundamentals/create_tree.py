class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)
        if self.root == None:
            self.root = new_node
            return True
        tmp = self.root
        while(1):
            if new_node.value == tmp.value:
                return False
            if new_node.value < tmp.value:
                if tmp.left == None:
                    tmp.left = new_node
                    return True
                tmp = tmp.left
            else:
                if tmp.right == None:
                    tmp.right = new_node
                    return True                          
                tmp = tmp.right
    def search(self,value):
        if self.root is None:
            return False
        tmp = self.root
        
        while tmp is not None:
            if value < tmp.value:
                tmp = tmp.left
            elif value > tmp.value:
                tmp = tmp.right
            else:
                return True
        return False
            
tree = BST()
tree.insert(5)
tree.insert(3)
tree.insert(7)

print("root:", tree.root.value)
print("left:",tree.root.left.value)
print("right:",tree.root.right.value)
print(tree.search(0))