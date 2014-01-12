#find whether there is a loop in a linked list

#First implement a linked list

class Node: 
    def __init__(self,value,NextNode=None):
        self.value =value
        self.next = NextNode
    
    def setNext(self,NextNode):
        self.next = NextNode
        
    def getNext(self):
        return self.next
    
    def getValue(self):
        return self.value
        
    
class LinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
        self.list=[]
    
    def getHead(self):
        return self.head
    
    def getTail(self):
        return self.tail
        
    def getSize(self):
        return len(self.list)
    
    def insert(self,val):  
        node = Node(val,None)
        
        self.list.append(node)
        #print self.getSize()
        if self.getSize()==1:
            self.head=node
            self.tail=node
            
        else:
            self.tail.setNext(node)
            self.tail=node
        
        
            
# linked list without a loop
L = LinkedList()
L.insert(10)
L.insert(20)
L.insert(30)
L.insert(40)

# let's create a linked list with a  loop

M = LinkedList()
M.insert(10)
M.insert(20)
M.insert(30)
M.insert(40)

M.head.getNext().getNext().setNext(M.head.getNext())


# is there a loop


def checkForLoops(list):
    slow = list.getHead()
    fast = slow.getNext()
      
    while True:        
        if slow==None or fast==None:
            return False
        elif slow==fast:
            return True
        else:
            slow = slow.getNext()
            if fast.getNext()!=None:
                fast = fast.getNext().getNext()
            else:
                fast  = fast.getNext()

# is there a loop in a linked list
print checkForLoops(L)
print checkForLoops(M)