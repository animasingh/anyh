# merge sort

def merge_sort(A,a,b):
	
	m = (a+b)/2;
	if m == a:
		return
		
	merge_sort(A,a,m)
	merge_sort(A,m,b)
	merge(A,a,m,b)
	#print A


def merge(A,a,m,b):

	list1 = A[a:m];
	list2 = A[m:b];
	#print list1
	#print list2
	
	for i in range(a,b):
		
		if list1 and list2: #if both lists are not empty
			if list1[0]<list2[0]:
				A[i]=list1.pop(0);
			else:
				A[i]=list2.pop(0);
					
		elif list1 and not list2: # if list2 is empty
			A[i:b] = list1;
			return
	
		elif not list1 and list2: # if list1 is empty
	 		A[i:b]=list2;
	 		return
	

A=[5,1,6,10,2,100,51,0];

print('Original list:\n')
print A

merge_sort(A,0,len(A))
print('Sorted list:\n')
print A

	
#A = [4,5,1,2,3];
#merge(A,0,2,len(A))
#print A

#A = [1,2,9,3,4,5];
#merge(A,0,3,len(A))
#print A

#A=[1]
#merge(A,0,0,0)
#print A

#Merge sort: sort in place
#A=[5,4,3,2,1];
#print('Original list:\n')
#print A

#A= merge_sort(A);
#print('After sorting:\n')
#print A