## Trees

Trees in Python are non-linear data structures having a root and nodes. Tree traversals refers to visiting each node present in a tree exactly once in order to update or check them.

         1
        /  \
       2    3
      /  \
     4    5       A tree.

Based on the order of visiting nodes in a tree, there are 3 types of tree traversals.Namely: In-Order Traversal, Pre-Order Traversal & Post-Order Traversal.


```python
#code example

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
```

### Types of Tree Traversals

**In-Order traversal** refers to visiting the *left nodes* followed by the *root* and then the *right nodes*.


```python
#An In-Order Traversal function
def InOrd(root):
    if root:
        InOrd(root.childleft)
        print(root.nodedata)
        InOrd(root.childright)
        
InOrd(root)
```

    4
    2
    5
    1
    3


**Pre-Order Traversal** refers to visiting the *root nodes* followed by the *left nodes* and then the *right nodes*


```python
#A pre-order traversal fuction
def PreOrd(root):
    if root:
        print(root.nodedata)
        PreOrd(root.childleft)
        PreOrd(root.childright)
        
PreOrd(root)
```

    1
    2
    4
    5
    3


**Post-Order Traversal** refers to visiting the *left nodes* followed by the *right-nodes* then the *root nodes*


```python
#A post-ord traversal function
def PostOrd(root):
    if root:
        PostOrd(root.childleft)
        PostOrd(root.childright)
        print(root.nodedata)
        
PostOrd(root)
```

    4
    5
    2
    3
    1

