class BinaryTreeNode:
    def __init__(self,data):
        self.root = data
        self.left = None
        self.right = None

btn1 = BinaryTreeNode(1)
btn2 = BinaryTreeNode(2)
btn3 = BinaryTreeNode(3)

btn1.left = btn2
btn1.right = btn3

print("root:",btn1.root)
print("root-left:",btn1.left.root)
print("root-right:",btn1.right.root)