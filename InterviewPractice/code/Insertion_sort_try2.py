# insertion sort in place
a=[6,5,2,4,1,10,100];

for i in range(1,len(a)): 
    j=i-1;
    key = a[i];
    
    while j>=0 and a[j]>key:
       a[j+1]=a[j];
       j=j-1;
           
    a[j+1]=key;

print a;

	
    
        
        
    
