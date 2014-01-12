# implement binary search tree

class Node:
    def __init__(self,value):
        self.value= value; 
        self.left = None;
        self.right=None; 
        
    def setLeft(self, Node):
        self.left = Node; 
    
    def setRight(self, Node):
        self.right = Node; 
    
    def getValue(self):
        return self.value; 
    
    def getLeft(self):
        return self.left;
    
    def getRight(self):
        return self.right;
        
        
class BinaryTree:
    
    def __init__(self):
        self.root =None;
    
    def getRoot(self):
        return self.root;
    
    def insert(self,value):
        if self.root==None:
            self.root = Node(value)
        else:
            self.insert_recursive(value,self.root);
        
    def insert_recursive(self, value, node):
                
        if value<=node.getValue():
            if node.getLeft()==None:
                node.setLeft(Node(value));
            else:
                self.insert_recursive(value,node.getLeft());
        
        if value>node.getValue():
            if node.getRight()==None:
                node.setRight(Node(value));
            else:
               self.insert_recursive(value,node.getRight());
                
    
    def search(self,value):
        if self.root==None:
            print 'Not Found';
        else:
            self.recursive_search(value,self.root);
            
    def recursive_search(self,value,node):
        
        if node== None:
            print 'Not Found';
        else:
            if value==node.getValue():
                print 'Found!';
            elif value< node.getValue():
                self.recursive_search(value,node.getLeft());
            elif value>node.getValue():
                self.recursive_search(value,node.getRight());
    
        
    def traverse(self):
        #return a sorted list of the items in the tree (smallest to largest).
        return self.traverse_recursive(self.root);
        
    
    def traverse_recursive(self,node):
        if node==None:
            return;
        
        self.traverse_recursive(node.getLeft());
        print node.getValue();
        self.traverse_recursive(node.getRight());
        
    def preorder_rec(self,node):
        if node==None:
            return
        print node.getValue()
        self.preorder_rec(node.getLeft())
        self.preorder_rec(node.getRight())

    def preorder_traverse(self):
        self.preorder_rec(self.getRoot())
    

    
    
def compareNodes(node1, node2):
    if node1==None and node2==None:
        return 0;
    elif node1!=None and node2!=None:
        if node1.getValue()==node2.getValue():
            return 0;
        else:
            return 1;
    else:
        return 1
        
    
        
        
def compareTrees(Tree1, Tree2):
    f=compareTrees_recursive(Tree1.getRoot(),Tree2.getRoot());
    if f:
        print 'They are identical';
    else:
        print 'They are NOT identical';
        
             
def compareTrees_recursive(Node1, Node2): 
    if Node1==None and Node2==None:
        return True;
          
    if Node1.getValue()!=Node2.getValue():
        return False;
    else:
        left = compareTrees_recursive(Node1.getLeft(),Node2.getLeft());
        if left==True:
            right = compareTrees_recursive(Node1.getRight(),Node2.getRight());
            return left and right;
        else:
            return left;

            
            
T=BinaryTree();
T.insert(10);
T.insert(20);
T.insert(50);
T.insert(5);
T.insert(4);
T.insert(100);

S=BinaryTree();
S.insert(10);
S.insert(20);
S.insert(50);
S.insert(5);
S.insert(4);
S.insert(100);

Q=BinaryTree();
Q.insert(10);
Q.insert(50);
Q.insert(20);
Q.insert(5);
Q.insert(4);
Q.insert(100);



R=BinaryTree();
R.insert(10);
R.insert(5);
R.insert(4);
R.insert(50);
R.insert(100);
R.insert(20);

Z=BinaryTree();
Z.insert(10);
Z.insert(20);
Z.insert(50);
Z.insert(4);
Z.insert(5);
Z.insert(100);


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

W.preorder_traverse()
    
    
 
        
        

        
        
        