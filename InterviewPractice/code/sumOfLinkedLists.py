from LinkedListAmazon import * 

# note we can use remainder and division to get carry and value
# carry = SUM/10
# value to insert = remainder(SUM,10)

def sumLL(node1, node2):
    newLL = LinkedList()
    carry = 0 
    return sumLL_rec(node1, node2, carry, newLL)
    
def sumLL_rec(node1, node2, carry, newLL):
    if node1==None and node2==None:
        if carry==1:
            newLL.insert(1)
        return newLL
        
    elif node1==None and node2!=None:
        S = node2.getValue()+carry
        carry = S/10
        digit = S%10
        newLL.insert(digit)
        
        '''
        if carry==0:
            newLL.insert(node2.getValue())
        elif carry==1:
            if node2.getValue()<9:
                newLL.insert(node2.getValue()+1)
                carry=0
            else:
                newLL.insert(0)
                carry=1
       '''
            
        return sumLL_rec(node1, node2.getNext(), carry, newLL)
    
    elif node1!=None and node2==None:
        
        S = node1.getValue()+carry
        carry = S/10
        digit = S%10
        newLL.insert(digit)
        
        #if carry==0:
        #    newLL.insert(node1.getValue())
        #elif carry==1:
        #    if node1.getValue()<9:
        #        newLL.insert(node1.getValue()+1)
        #    else:
        #        newLL.insert(0)
        #        carry=1
                
        return sumLL_rec(node1.getNext(), node2, carry, newLL)
    
    elif node1!=None and node2!=None:
        S = node1.getValue()+ node2.getValue()+carry
        carry = S/10
        digit = S%10
        newLL.insert(digit)
        return sumLL_rec(node1.getNext(), node2.getNext(), carry, newLL) 
        
    
L1 = LinkedList()
L2 = LinkedList()

L1.insert(3)
L1.insert(1)

L2.insert(0)
L2.insert(9)
L2.insert(1)

resLL= sumLL(L1.getHead(), L2.getHead())
n = resLL.getHead()
while n!=None: print n.getValue(); n=n.getNext()
print '-----'
L1 = LinkedList()
L2 = LinkedList()

L1.insert(9)
L1.insert(9)

L2.insert(9)
L2.insert(9)

resLL= sumLL(L1.getHead(), L2.getHead())
n = resLL.getHead()
while n!=None: print n.getValue(); n=n.getNext()