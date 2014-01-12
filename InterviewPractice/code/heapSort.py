A = [9,2,5,3];
# implement heap sort

class Heap:   
    def __init__(self,list=[]):
        self.list=list;
        if list!=[]:
            for i in list:
                self.Insert(i)
                    
    def Insert(self,item):
        self.list.append(item)
        idx = self.heapSize()-1;
        
        while idx!=0 and self.parent(idx)>=0 and self.list[self.parent(idx)]<item:
            
            self.list[idx] = self.list[self.parent(idx)]  
            idx = self.parent(idx)
            
        self.list[idx]=item
        
    def leftChild(self,i):
        return i*2+1;

    def rightChild(self,i):
        return i*2+2

    def parent(self,i):
        return i/2 -1

    def max(self):
        return self.list[0]
    
    def extractMax(self):
        m = self.max()
        self.list[0]=self.list[-1];
        self.pop()
        self.Heapify(0)
        return m
        
    def Heapify(self,index):
        lidx = self.leftChild(index)
        ridx = self.rightChild(index)
        
        if lidx<len(self.heapSize()) and self.list[lidx]>self.list[index]:
            largest= lidx
        else:
            largest= index
        
        if ridx<len(self.heapSize()) and self.list[ridx]>self.list[index]:
            largest = ridx
        else:
            largest = index
        
        if largest != index:
            largestvalue = self.list[largest]
            self.list[largest]=self.list[index]
            self.list[index]= largestvalue
            self.Heapify(largest)
 
    def heapSize(self):
        return len(self.list)   



def heapSort(A):    
    s=[]
    heap = Heap(A);
    while heap.heapSize()>0:  
        s.append(heap.extractMax())        
    return s
    








