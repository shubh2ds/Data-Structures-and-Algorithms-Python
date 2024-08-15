class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None
    def __insert(self, current_node,value):
        if current_node == None:
            return Node(value)
        if current_node.value == value :
            return None
        if current_node.value > value:
            current_node.left = self.__insert(current_node.left,value)
        elif current_node.value < value:
            current_node.right= self.__insert(current_node.right,value)
        return current_node

    def insert(self,value):
        new_node = Node(value)
        if self.root == None:
            self.root = new_node
        self.__insert(self.root, value)
    
    def __delete(self,current_node , value):
        if current_node == None:
            return None
        if current_node.value > value:
            current_node.left = self.__delete(current_node.left, value)
        elif current_node.value < value:
            current_node.right = self.__delete(current_node.right, value)
        else:
            if current_node.left == None and current_node.right == None:
                return None
            if current_node.left == None:
                current_node = current_node.right
            if current_node.right == None:
                current_node = current_node.left
            
            #dlt from subtree
            sub_tree_min = self.get_min(current_node.right)
            current_node.value = sub_tree_min
            current_node.right = self.__delete(current_node.right , sub_tree_min)

        return current_node
    
    def delete(self,value):
        if self.root == None:
            return None
        self.__delete(self.root , value) 

    def dfs1(self):
        if self.root == None:
            return None
        queue = []
        results = []
        queue.append(self.root.value)
        while len(queue) != 0:
            current = queue.pop(0) 
            results.append(current.value)
            if current.left != None:
                queue.append(current.left)
            if current.right != None:
                queue.append(current.right)
        return results
    def dfs_preorder(self):
        results = [] # root -> left complete till none -> then right
        def trav(current):
            results.append(current.value)#root
            if current.left !=None:#left
                trav(current.left)
            if current.right !=None: #right
                trav(current.right)
            
        trav(self.root)
        return results
    
    def dfs_postorder(self):
        results = [] # root -> left complete till none -> then right
        def trav(current):
            
            if current.left !=None:#left
                trav(current.left)
            if current.right !=None: #right
                trav(current.right)
       
            results.append(current.value)#root    
        trav(self.root)
        return results
    

tree = BST()
tree.insert(47)     
tree.insert(21)      
tree.insert(76) 

tree.insert(18)     
tree.insert(27)      
tree.insert(52)
tree.insert(82)
print(tree.root.value)       
print(tree.root.left.value)    
print(tree.root.right.value)  

#tree.delete(7)
#print("after delete")
# print(tree.root.value)       
# print(tree.root.left.value)    
# print(tree.root.right.value) 

print(tree.dfs_preorder())
#OP: [47, 21, 18, 27, 76, 52, 82]

print(tree.dfs_postorder())
