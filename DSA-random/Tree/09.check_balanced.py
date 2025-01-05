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

def heightOfTree(root):
    if root == None:
        return 0
    return 1+ max( heightOfTree(root.left), heightOfTree(root.left) )

def checkBalanced(root):
    if root == None:
        return True
    if (heightOfTree(root.left) - heightOfTree(root.right)>0) or (heightOfTree(root.right) - heightOfTree(root.left)>0):
        
        return False
    
    if checkBalanced(root.left) and checkBalanced(root.right):
        
        return True
    else:
        return False
    
root = inputToTree()
print("Tree:")
printTreeDetailed(root)
if checkBalanced(root):
    print("Tree is Balanced!")
else:
    print("Tree is not Balanced!")

"""
Enter node value:1
Enter node value:2
Enter node value:-1
Enter node value:-1
Enter node value:3
Enter node value:-1
Enter node value:4
Enter node value:-1
Enter node value:-1
Tree:
1:2 , 3
2:
3:4
4:
Tree is not Balanced!
PS D:\Git\Data-Structures-and-Algorithms-Python> & C:/Users/shubh/anaconda3/envs/venv2/python.exe d:/Git/Data-Structures-and-Algorithms-Python/Tree/check_balanced.py
Enter node value:1
Enter node value:2
Enter node value:-1
Enter node value:-1
Enter node value:3
Enter node value:-1
Enter node value:-1
Tree:
1:2 , 3
2:
3:
Tree is Balanced!
PS D:\Git\Data-Structures-and-Algorithms-Python> & C:/Users/shubh/anaconda3/envs/venv2/python.exe d:/Git/Data-Structures-and-Algorithms-Python/Tree/check_balanced.py
Enter node value:1
Enter node value:2
Enter node value:-1
Enter node value:3
Enter node value:-1
Enter node value:-1
Enter node value:4
Enter node value:-1
Enter node value:-1
Tree:
1:2 , 4
2:3
3:
4:
Tree is not Balanced!
"""