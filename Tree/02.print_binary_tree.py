class BinaryTreeNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

btn1 = BinaryTreeNode(1)
btn2 = BinaryTreeNode(2)
btn3 = BinaryTreeNode(3)

btn1.left = btn2
btn1.right = btn3

def printTree(root, type='Root'):
    if root == None:
        return None
    print(type,":",root.data)
    printTree(root.left, 'L')
    printTree(root.right, 'R')

def printTreeDetailed(root):
    if root == None:
        return
    print(root.data,end=': ')
    if root.left !=None:
        print('L:', root.left.data, end = ', ')
    if root.right !=None:
        print('R:', root.right.data, end='')
    print()
    printTreeDetailed(root.left)
    printTreeDetailed(root.right)


printTreeDetailed(btn1)