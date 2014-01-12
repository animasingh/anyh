#listA and listB are sorted

def sUnion(A,B):
    sunion=[]
    a=0
    b=0
    
    while True:       
        if a<len(A) and b<len(B):
            if A[a]<=B[b]:
                sunion.append(A[a])
                if A[a]==B[b]:
                    b=b+1
                a=a+1  
            elif A[a]>B[b]:
                sunion.append(B[b])
                b=b+1
                
        elif a<len(A) and b>=len(B):
            sunion=sunion+A[a:]    
            break
        elif b<len(B) and a>=len(A):
            sunion=sunion + B[b:]
            break     
    return sunion
    
A = [1,5,8,9]
B=[1,2,10]
print sUnion(A,B)