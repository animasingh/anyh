from BinarySearchTree import *

def Fliptree(node):
    if node==None:
        return   
    Fliptree(node.getLeft())
    Fliptree(node.getRight())
    temp = node.getRight()
    node.setRight(node.getLeft())
    node.setLeft(temp)
  

def ModifyTree(node):
    if node==None:
        return
    ModifyTree(node.getLeft())
    ModifyTree(node.getRight())
    #first flip the subtree
    temp = node.getRight()
    node.setRight(node.getLeft())
    node.setLeft(temp)
    # next add the left node to the rightmost child of the rightnode
    
    current = node
    rightMost  = node
    #get the rightmost node
    while rightMost.getRight()!=None:
        rightMost=rightMost.getRight()
    
    #Next add the left node as the right of the rightmost node
    rightMost.setRight(current.getLeft())
    current.setLeft(None)
    

B=BinaryTree()
B.insert(10)
B.insert(5)
B.insert(11)
B.insert(2)
B.insert(6)

print B.preorder_traverse()
ModifyTree(B.getRoot())
print B.traverse()


#Fliptree(B.getRoot())


