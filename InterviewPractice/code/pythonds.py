class Vertex:
    
    def __init__(self,id):
        self.id = id
        self.connectedTo={};
        
    def addNeighbor(self,Vertex,weight=1):
        self.connectedTo[Vertex]=weight;
        
    def __str__(self):
        return str(self.id) + ' is connected to'  + str([x.id for x in self.connectedTo])
        
    def getConnections(self):
        return self.connectedTo.keys()
    
    def getId(self): 
        return self.id
        
    def getWeight(self,Vertex):
        return self.connectedTo[Vertex]
        

class Graph:
    
    def __init__(self):
        self.numVertices=0
        self.vertList={}
        
    def addVertex(self,key):
        v = Vertex(key)
        self.numVertices+=1
        self.vertList[key]=v
        return v
    
    def getVertex(self,key):
        if key in self.vertList:
            return self.vertList[key]
        else:
            None
            
    def addEdge(self,id1,id2, edgeWt):
        if id1 not in self.vertList:
            self.addVertex(id1)
        if id2 not in self.vertList:
            self.addVertex(id2)  
        self.vertList[id1].addNeighbor(self.vertList[id2])
        
    def getVertices(self):
        return self.vertList.keys()
        
        
    def __iter__(self):
        return iter(self.vertList.values())
    
   
        
    