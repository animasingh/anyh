# data structures in python

# we could use lists for stacks. 
s = [];
s.append(6) #append is equivalent to push
s.append(7)
s.pop() # pop

# we can use lists for queue
s=[3,4,5,6,7];
s.append(77) # queueing
s.append(88)
s=s[1:];
# but lists are not efficient to be used as a queue since when we remove the 
# item from the beginning all the following items has to be moved. 
# Therefore, python has a queue in collections that we can use with fast appends 
# pops from both ends

from collections import deque

a = deque([9,10,11,34]);
a.append("anima")
a.popleft()
a.popleft()

# functional programming tools.
# builtin functions that are very useful when used with lists. 
# 1. filter() 2.map() and 3.reduce()
# filter(function,list) -- only display items of the list that for which the function is true. 
def divisible(x):
    return x % 2 ==0 and x % 3==0;
a=range(0,30); 
filter(divisible,a)

# 2. map(function, list) --displays function(item) for each item in the list

def cube(x):
    return x**3;
a=range(0,4);
map(cube,a)

# 3. List comprehensions. 
cubes = [x**3 for x in range(0,4)];

[(x,y) for x in [1,2,3] for y in [3,1,4] if x!=y]


# dictionaries
knights = {'gallahad': 'the pure', 'robin': 'the brave'}

for k,v in knights.iteritems():
    print k,v

