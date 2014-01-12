# implement quicksort


def quicksort(A,p,r):
	q = partition(A,p,r)
	quicksort(A,p,q)
	quicksort(A,q+1,r)
	

def partition(A,p,r):
	pivot = A[p]
	
	i=p
	j=r
	
	print i,j
	
	while True:
	        if A==[1,2,5,7]:
	           print i,j
	           break
	           
	        print pivot
		while A[j]>pivot and j>=0:
			j=j-1
			print "j:",j 
			
		while A[i]<pivot and i>=0:
			i=i+1
			print "i:", i
			
		if i<j:
			b = A[j]
			A[j] = A[i]
			A[i] = b
			#A[i],A[j] = A[j], A[i]
			
		else:
			return i

A=[7,2,5,1]
quicksort(A,0,len(A)-1)


A=[7,2,5,1]
p=0
r=len(A)-1
pivot=A[p]

i=p
j=r

print pivot
A[j]>pivot
A[i]<pivot
