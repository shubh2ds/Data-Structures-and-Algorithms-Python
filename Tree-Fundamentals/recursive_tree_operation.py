class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert1(self,value):
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
    def search_recursive(self, root, value):
        if root == None:
            return False
        if root.value == value:
            return True

        elif root.value > value:
            return self.search_recursive(root.left, value)
        elif root.value < value:
            return self.search_recursive(root.right, value)

    def search(self, value):
        return self.search_recursive(self.root, value)
    
    def __insert_recursive(self, current_node, value):
        if current_node == None:
            return Node(value)
        if current_node.value > value:
            current_node.left =  self.__insert_recursive(current_node.left, value)
        if current_node.value < value:
            current_node.right =  self.__insert_recursive(current_node.right, value)
        return current_node

    def insert(self, value):
        if self.root == None:
            self.root = Node(value)
        self.__insert_recursive(self.root, value)

tree = BST()
tree.insert(5)
tree.insert(3)
tree.insert(7)
print(tree.root.value)
print(tree.root.left.value)
print(tree.root.right.value)
print(tree.search(7))