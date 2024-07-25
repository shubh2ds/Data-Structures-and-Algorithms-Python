class BinaryTreeNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def printTreeDetailed(root):
    if root == None:
        return 
    print(root.data, end=':')

    if root.left !=None:
        print(root.left.data,end=' , ')
    if root.right !=None:
        print(root.right.data,end='')
    print()

    printTreeDetailed(root.left)
    printTreeDetailed(root.right)

def inputToTree():
    n = int(input("Enter node value:"))
    if n == -1:
        return None
    root = BinaryTreeNode(n)
    root.left = inputToTree()
    root.right = inputToTree()
    
    return root

def removeLeafNode(root):
    if root == None:
        return None
    if root.left ==None and root.right == None:
        return None

    root.left = removeLeafNode(root.left)
    root.right = removeLeafNode(root.right)
    return root

root = inputToTree()
print("Tree:")
printTreeDetailed(root)
root = removeLeafNode(root)
print("Tree after removing leaves:")
printTreeDetailed(root)