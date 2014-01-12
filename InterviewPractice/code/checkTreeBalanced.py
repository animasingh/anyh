def getHeight(node): 
     # base case

     if node == None: 
          H = 0
          return H
     
     else:
          leftHeight = 1 + getHeight(node.getLeft())
          rightHeight = 1 + getHeight(node.getRight())

          if leftHeight != rightHeight:
               print 'Tree is unbalanced'
               return -1
          else:
               # if leftHeight and rightHeight are the same, return the height
               return leftHeight
               
from BinarySearchTree import *

Q = BinaryTree()
Q.insert(5)
Q.insert(2)
Q.insert(10)
Q.insert(1)
Q.insert(3)


W= BinaryTree()
W.insert(5)
W.insert(2)
W.insert(10)
W.insert(1)
W.insert(3)
W.insert(8)
W.insert(13)

print getHeight(Q.getRoot())
print getHeight(W.getRoot())


    