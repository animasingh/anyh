def reverseString(s):
    r='';
    for i in range(len(s)-1,-1,-1):
            r=r+s[i];
    print r;
    
reverseString('anima')

def reverseString_recursive(s):
    if len(s)==1:
        return s;
    return s[-1]+reverseString_recursive(s[:-1]);

''' this print the nth fibonacci number. '''
def fibonacci(n):
    if n==0:
            return 0;
    elif n==1:
            return 1;
    return fibonacci(n-1)+fibonacci(n-2);
    
''' the following prints out the list of fibonacci numbers'''       
for i in range(0,11):
    print fibonacci(i);
    
  
''' print out the multiplication table upto 12X12'''
''' this uses lists'''
for i in range(1,13):
    print [i*j for j in range(1,13)]; ''' this is called list comprehensions'''

'''we can also do it using arrays'''
import numpy as np;
for i in range(1,13):
        print np.array(range(1,13))*i;
        
''' the above does the trick. But it does not return the output in a well-formatted fashion'''
''' the code below does pretty formatting'''
for i in range(1,13):
    A=[i*j for j in range(1,13)]; ''' this is called list comprehensions'''
    table = '';
    for item in A:
        table = table +' {:3}'.format(item);
    print table

''' Write a function that sums up integers from a text file, one int per line.'''
'''Reading files'''
f=open('integerList.csv');
s=0;
for line in f.readlines():
    s=s+int(line)
print "The sum is {}".format(s);

''' print odd numbers from 1 to 99'''
for i in range(1,6,2):
        print i;

''' Find the largest integer value in an integer array'''
L=[1,100,5,2,50];
max=-inf;
for item in L:
    if item>max:
            max= item;
print max;

        
