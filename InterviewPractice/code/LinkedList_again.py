class Node: 
	def __init__(self,value):
		self.value = value
		self.prev = None
		self.next = None

class LinkedList:
	def __init__(self):
	 	self.Head=None
		self.Tail=None


	def insert(self,value):
		node = Node(value) 
		# insert node at the head
		if self.Head==None:
		    self.Head=node
		else:
		    node.next = self.Head
		    self.Head.prev = node
		    self.Head = node

	def search(self,value):
            node = self.Head 
            
            while node!= None: 
                print node.value
                if node.value==value: 
	           return node
                node = node.next
            return None

	def delete(self,value):
		n = self.search(value)
		if n==None: 
		  print "Value is not in the list"
		else:
		    if n!=self.Head:
		        n.prev.next = n.next
		        n.next.prev = n.prev
		        print "Value is deleted"
		    else:
		        self.Head=n.next
		        n.prev = None
		        
		        
def findNtoLast(LL,n):
     p1=LL.Head
     p2=LL.Head
     
     #print p1.value
     #print p2.value
     
     for i in range(0,n-1):
         if p2==None: 
             print "The list is smaller than",n
             return
         else:
             p2=p2.next
     
     #print p1.value
     #print p2.value 
     while p2.next!=None:
        p1=p1.next
        p2=p2.next
        #print p1.value
        #print p2.value
     return p1
             	      
		  
		    
		    