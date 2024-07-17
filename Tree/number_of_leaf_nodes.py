class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def printTreeDetailed(root):
    if root == None:
        return
    print(root.data, end =':')
    if root.left !=None:
        print("L:", root.left.data , end=", ")
    if root.right !=None:
        print("R:", root.right.data , end="")
    print()
    printTreeDetailed(root.left)
    printTreeDetailed(root.right)

# btn1 = BinaryTreeNode(1)
# btn2 = BinaryTreeNode(2)
# btn3 = BinaryTreeNode(3)
# btn1.left = btn2
# btn1.right = btn3
#printTreeDetailed(btn1)

def input_to_tree():
    rootData = int(input("Enter value:"))
    if rootData == -1:
        return None
    root = BinaryTreeNode(rootData)
    print("=== Left ====")
    root.left = input_to_tree()
    print("=== Right ===")
    root.right = input_to_tree()
    return root

def count_leaf_nodes(root):
    if root == None:
        return 0
    if root.left == None or root.right == None:
        return 1
    
    return count_leaf_nodes(root.left) + count_leaf_nodes(root.right)
    

root = input_to_tree()
printTreeDetailed(root)
leaf_nodes = count_leaf_nodes(root)
print("leaf_nodes:",leaf_nodes)