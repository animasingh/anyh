#Insertion sort: sort in place
A=[5,4,3,2,1];
print A
for j in range(1,len(A)):
	#print j
	key = A[j];
	i=j-1;
	while i>=0 and A[i]>key:
		A[i+1]=A[i];
		i=i-1;
		
	A[i+1]=key
	
	
print('After sorting:\n')
print A

