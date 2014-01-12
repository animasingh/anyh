# selection sort in place

a=[6,5,2,4,1,10,100];


for i in range(0,len(a)):
    min= a[i];
    
    for j in range(i+1,len(a)):
        if a[j]< min:
            a[i]=a[j];
            a[j]= min;
            min = a[i];
            
print a

    

            
            
    

