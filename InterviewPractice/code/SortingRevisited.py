# selection sort

A=[5, 1, 4, 10, 3 ,8]; 


def selectionSort(A):
    for i in range(0, len(A)):
        min = A[i]; 

        for j in range(i+1, len(A)):
            if A[j]<min:
                A[i]= A[j] # store the new minimum in the ith position
                A[j]= min # store the old minuimum in the j th position
                min = A[i] # update the minimum variable
    return A

#print A
#print selectionSort(A)

# Heap sort : It is basically selection sort but using a heap structure

class Heap:
    def __init__(self):
        self.list = []
    
    def showList(self):
        return self.list
    
    def size(self):
        return len(self.list)
    
    def parent(self,idx):
        return idx/2
    
    def left(self,idx):
        return 2*idx+1
        
    def right(self,idx):
        return 2*idx+2
        
    def insert(self,item):
        # first add the item to the list
        self.list.append(item)
        idx = self.size()-1
        # check if the heap property is satisfied 
        while idx!=0 and self.list[self.parent(idx)]> item :        
            self.list[idx] = self.list[self.parent(idx)]    
            idx = self.parent(idx)
        self.list[idx]=item
    
    def showMin(self):
        return self.list[0]
    
    def extractMin(self):
        
        min = self.showMin()
        # maintain heap structure
        lastKey = self.list.pop()
        
        if self.size()!=0:        
            #place the last item in the first slot
            self.list[0] = lastKey;
            #now we need to heapify it. Note that both left and right subtree of the root are heaps. 
            self.Heapify(0)
            
        return min
        
    def Heapify(self,idx):       
        leftidx = self.left(idx)
        rightidx = self.right(idx)
        
        minId= idx
        currKey= self.list[idx]
        
        #print idx, leftidx, rightidx, len(self.list), self.list, minId, idx
        if leftidx<self.size()-1 and self.list[leftidx]<self.list[minId] :
            #print idx, leftidx, rightidx, self.list[idx], self.list[leftidx], self.list[rightidx]
            minId = leftidx
            
        if rightidx<self.size()-1 and self.list[rightidx]<self.list[minId] :
            #print idx, leftidx, rightidx, self.list[idx], self.list[leftidx], self.list[rightidx]
            minId = rightidx
        
        if minId != idx:
            self.list[idx] = self.list[minId]
            self.list[minId] = currKey
            #print 'List:', self.list
            self.Heapify(minId)
            
       
    
def heapSort(A):    
    h = Heap() # first create a min-heap structure
    # insert all elements in the heap
    for item in A:
        h.insert(item)
        
    #now extract minimum from the heap and insert in A in a sorted manner
    for i in range(0,len(A)):
        A[i] = h.extractMin()
    
    return A
        

#print A
#print heapSort(A)



# implement insertion sort

A=[5, 1, 4, 10, 3 ,8]; 
for i in range(0,len(A)):
    key = A[i]
    j=i-1   
    while j>=0 and A[j]>key:
        A[j+1] =A[j];
        j=j-1    
    A[j+1] =key 
#print A
    

#Quick sort

# merge sort

A=[5, 1, 4, 10, 3 ,8]; 


    

