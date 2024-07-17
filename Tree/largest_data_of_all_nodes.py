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

def largest_data(root):
    if root == None:
        return 0
    return max( largest_data(root.left) , largest_data(root.right), root.data )
    

root = input_to_tree()
printTreeDetailed(root)
largest_data = largest_data(root)
print("largest_data:",largest_data)

"""
33:L: 44,
44:L: 22, R: 11
22:
11:
largest_data: 44
"""