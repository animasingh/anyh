from collections import deque

class Vertex:
	def __init__(self,value):
		self.value=value
		self.neighbors={}
		
	def addNeighbor(self,otherVertex,edgeweight):
		self.neighbors[otherVertex]=edgeweight
		 
	def getValue(self):
		return self.value
		
	def getNeighbors(self):
		return self.neighbors


class Graph:
	def __init__(self):
		self.vertices={}
		
	def size(self):
		return len(self.vertices)
		
	def addVertex(self,value):
		self.vertices[value]=Vertex(value)
		
	def getVertex(self,value):
	   if value not in self.vertices:
	       raise Exception
	   else:    
	       return self.vertices[value]
	   
	def addEdge(self,val1,val2,edgeweight):
		if val1 not in self.vertices:
			self.addVertex(val1)
			
		if val2 not in self.vertices:
			self.addVertex(val2)
		
		self.vertices[val1].addNeighbor(self.vertices[val2] ,edgeweight)
	
	
	def __str__(self):
		gstr=''
		for v in self.vertices:
			gstr = gstr + str(self.vertices[v].getValue()) + ' is connected to'  + str([x.getValue() for x in self.vertices[v].getNeighbors()]) + '\n'
		
		return gstr


        

        def shortest_path_length(self,start_val,end_val):
            if start_val not in self.vertices or end_val not in self.vertices:
                raise Exception
            
            Q = deque() # initialize a queue
            Q.append((start_val,0))
            
            while len(Q)>0:
                currV = Q.popleft()
                if currV[0] == end_val:
                    return currV[1]
                else:
                    for vertex in g.vertices[currV[0]].getNeighbors():
                        Q.append((vertex.getValue(),currV[1]+1))
            
            
            print "No path exists between {0} and {1}".format(start_val, end_val)
                    
                        
                
            
            
            
g=Graph()
g.addEdge("a","c",1)
g.addEdge("c","a",1)
g.addEdge("c","d",1)
g.addEdge("d","c",1)

g.addEdge("c","b",1)
g.addEdge("b","c",1)

g.addEdge("c","e",1)
g.addEdge("e","c",1)

g.addEdge("e","b",1)
g.addEdge("b","e",1)
g.addEdge("a","d",1)
g.addEdge("d","a",1)

g.addVertex("f")
	
	
	
		