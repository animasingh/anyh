# implemented a weighted graph class

class Vertex:
    def __init__(self,id):
        self.id = id
        self.neighbors = {}
    
    def getId(self):
        return self.id
    
    def addNeighbor(self,other,weight=1):
        self.neighbors[other]=weight
        
    def getNeighbors(self):
        return self.neighbors

    def getEdgeWeight(self,neighborVertex):
        if neighborVertex in self.neighbors:
            return self.neighbors(neighborVertex)
        else:
            return inf
        
        
class Graph:
    def __init__(self):
        self.numVertices=0
        self.vertexList={}
    
    def getNumVertices(self):
        return self.numVertices
                
    def addVertex(self,id):
        self.numVertices +=1
        
        if id not in self.vertexList:
            v = Vertex(id)
            self.vertexList[id]=v
        
    def addEgde(self, id1,id2,weight=1):
        if id1 not in self.vertexList:
            self.addVertex(id1)
        elif id2 not in self.vertexList:
            self.addVertex(id2)        
        self.vertexList[id1].addNeighbor(self.vertexList[id2],weight)  

    def getVertexList(self):
        return self.vertexList

class HeapNode:
    def __init__(self, id, value):
        self.id = id
        self.value = value
    def getId(self):
        return self.id
    def getValue(self):
        return self.value
    

class Heap:
    def __init__(self):
        self.List = []
    
    def getHeapSize(self):
        return len(self.List)
        
    def getParentIdx(self,idx):
        return idx/2 - 1
    
    def getLeftIdx(self,idx):
        return idx*2 + 1
        
    def getRightIdx(self,idx):
        return idx*2+2
    
    def insert(self,id,value): 
        heapNode = HeapNode(id,value)
        # if the value of the inserted heapNode is < than that of the Parent, then keep on going up
        self.List.append(heapNode)
        idx = self.getHeapSize()-1
        
        while idx!=0 and self.getParentIdx(idx)>=0 and self.List[self.getParentIdx(idx)].getValue() > heapNode.getValue():
            self.List[idx] = self.List[self.getParentIdx(idx)] # place the parent here
            idx = self.getParentIdx(idx)    
 
        self.List[idx] = heapNode     
            
    def min(self):
        return (self.List[0].getId() , self.List[0].getValue())
    
    def getList(self):
        return self.List
    
class PriorityQueue:
    def __init__(self):
        self.H = Heap();
    
    def extractMin(self):
        heapNode = self.H.extractMin()
        return (heapNode.getId(), heapNode.getValue())
    
    def insert(self,id,value):
        self.H.insert(id,value)
    
    def len(self):
        return self.H.getHeapSize()


def Dj(Graph,srcVertex,targetVertex):
    
    vertexList = Graph.getVertexList()
    Distance={}
    Previous={}
    
    PQ = PriorityQueue()
    
    for id in vertexList:
        vertex = vertexList[id]
        Previous[vertex]=None
        if vertex == srcVertex:
            Distance[vertex]=0
        else:
            Distance[vertex]=inf
                 
        # add each vertex to a PQ
        PQ.insert(id,Distance[vertex])
     
    while PQ.len()>0:
        # extract the node with the minimum distance  
        (currId, currValue) = PQ.extractMin()
        currVertex = vertexList[currId] 
         
        if currVertex == targetVertex:
            return (Previous, Distance)
        #visit all neighbors of the currVertex
        for neighbor in currVertex.getNeighbors():
            newDistance = Distance(currVertex) + currVertex.getEdgeWeight(neighbor)
            if newDistance < Distance[neighbor]:
                Distance[neighbor]=newDistance
                Previous[neighbor] = currVertex 
        
        # remove currVertex from unvisitedVertices 
        del vertexList[currId]           
   
    return (Previous, Distance)
   


(Previous, Distance) = Dj (Graph, srcVertex, targetVertex)
# what's the shortest distance between srcVertex and targetVertex
print Distance[targetVertex]

#what is the shortest path



H = Heap()
H.insert(1,10)
H.insert(2,50)
H.insert(3,-10)