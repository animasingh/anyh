# check if there are two number in an array that add up to X

A = [ 5, 8, 3, 2, 1];
# if A is unsorted
def checkSum(A,num):
    for i in range(0,len(A)):
        for j in range(i,len(A)):
            if A[i]+A[j]==num:
                 return True
    
    return False
    

print checkSum(A,5)
print checkSum(A,12)

# time complexity is O(n^2)


#assume that A is sorted. The complexity is O(n)
def checkSum(A,num):
    s = 0
    e=len(A)-1
    
    numTimes=0
    
    while s<e:
        print A[s]+A[e], s,e
        if A[s]+A[e]==num:
            numTimes+=1
            s=s+1
        elif A[s]+A[e]>num:
            e=e-1
        elif A[s]+A[e]<num:
            s=s+1
            
        
    return numTimes

A=[-1,0,1,3,4,9,10]
print checkSum(A,4)