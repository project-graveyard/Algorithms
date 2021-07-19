#creating a node class

class Node:
    def __init__(self, val):
        self.childleft = None
        self.childright = None
        self.nodedata = val
        
#creating an instance of the Node class and converting it to a tree
root = Node(1)
root.childleft = Node(2)
root.childright = Node(3)
root.childleft.childleft = Node(4)
root.childleft.childright = Node(5)

#An In-Order Traversal function
def InOrd(root):
    if root:
        InOrd(root.childleft)
        print(root.nodedata)
        InOrd(root.childright)
        
InOrd(root)
