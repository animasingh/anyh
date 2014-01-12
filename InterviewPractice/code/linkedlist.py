class Node:
	def __init__(self,value):
		self.value = value; 
		self.next = None
	
	def __str__(self):
		return str(self.value);
	 

class linkedlist:
	def __init__(self ):
		self.head= None; 
		
		
		
	def insert(self, value):
		new_node = Node(value); 
		
		if self.head== None:
			self.head = new_node
		else:
			new_node.next = self.head;
			self.head = new_node;
		    
	
	def remove(self,value):
		curr_node = self.head; 
		prev_node = None;
		
		while curr_node!= None:
			if curr_node.value==value:
				if prev_node==None:
					self.head = curr_node.next;
				else:
					prev_node.next = curr_node.next;
			prev_node = curr_node;
			curr_node = curr_node.next;	
				
					
	def __str__(self):
		curr_node = self.head;
		list='';
		while curr_node!=None:
			list+= str(curr_node.value)+',';
			curr_node = curr_node.next;
		return list;	
				
			
		
ll = linkedlist();
ll.insert(5)
ll.insert(10)
print ll
ll.remove(5)
print ll
ll.remove(1)
print ll
ll.remove(10)
print ll
		
		