# are there any duplicates in a list?

a=[10,11,4,2,1,100,10,200];
a.sort()
for i in range(1,len(a)):
    if a[i]==a[i-1]:
        print 'Yes there are duplicates!'
        break
        
#Examples of hash functions
s='anima'
hash=1; 
for c in s:
        hash = 101*hash + ord(c); 


# check if two sets A and B are disjoint 
#use hash table.

A=[5,3,2,6,1,4]
B=[7,8,50]

d={}

for item in A:
    if item in d:
        pass
    else:
        d[item]=1
        

for item in B:
    if item in d:
        print 'Sets are not disjoint';
        break
        
def comparator(x,y):
    return x-y

A.sort(comparator)

array = [8, 2, 9, 0, 1, 2, 5];
def comparator2(x, y):
    ## Just a condition for example,
    ## you can add as many you need.
    if(x % 2):
        return x
    return x-y
    
array = [8, 2, 9, 0, 1, 2, 5];
array.sort(comparator2)
print array




 

