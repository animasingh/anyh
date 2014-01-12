from pythonds import Graph
from pythonds import Vertex 
from pythonds.basic import Queue # this does not exist. I am assuming that we
# have an implementation for queue.

def buildGraph(wordFile):
    f= open(wordFile,'r')
    g = Graph()
    d={}
    
    for line in f.readlines():
        word = line[:-1]
        for i in range(0,len(word)):
            bucket = word[:i]+'_'+word[i+1:]
            if bucket in d:
                d[bucket].append(word)
            else:
                d[bucket]=[word]
        
        for bucket in d:
            for word1 in bucket:
                for word2 in bucket:
                    g.addEdge(word1,word2)     
    return g
    

# all vertices are initialized as "white" -> undiscovered

def bfs(graph, startVertex):
    startVertex.parent(None)
    startVertex.setDistance(0)
    startVertex.setColor('gray')
    Q = Queue();
    Q.enqueue(startVertex)
    while Q.size()>0:
        currVertex = Q.deque()
        for v in startVertex.getConnections():
            if v.getColor=='white': #not discovered yet
                v.setColor('gray') # discovered now
                v.setDistance(currVertex.getDistance()+1)
                v.parent(currVertex)
                Q.enqueue(v)
        currVertex.setColor('black')  
        


def dfs(graph,v):
        v.setColor('gray')
        time = time+1
        v.setDiscovery(time)
        for vc in v.getConnections():
            if vc.getColor()=='white':
                vc.parent(v)
                dfs(graph.vc)
        v.setColor('Black')
        time=time+1
        v.setExit(time)
        
        
        
        
def updateTimer(timer):
    if timer<=5:
            timer=timer+1
            updateTimer(timer)
    else:
        print timer
        return 
        

def ListAppend(L):
    if len(L)<=5:
        L.append(1)
        ListAppend(L)
    else:
        return
        
            
              
                
                    
        
        
        



    
    
    
    