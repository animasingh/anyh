# reverse words in a string
# we could do it by splitting the string into words. and then scanning the list of words in the reverse order. 
# we need to create a temporary buffer to store the words as we scan the list in the opposite order

# how can we reverse words in a string using no temporary buffer of size n?
# First: reverse the entire string in place by exchanging characters
# Second: the words are now in the order we want. But the characters within the words are in the reverse order. 


string = 'this is anima'
string = [s for s in string]

#reverse in place



def reverseString(string,startIndex,endIndex):
    j=endIndex
    for i in range(startIndex,endIndex+1):
        if j<=i:
            break
        temp = string[i]
        string[i]= string[j]
        string[j]=temp   
        j=j-1


print string
# first reverse the entire string in place
reverseString(string,0,len(string)-1)
print string
# second reverse each word in place
stidx=0
for i in range(1,len(string)):
    if string[i]==' ':
        eidx=i-1
        reverseString(string,stidx,eidx)
        stidx = i+1
    elif i==len(string)-1:
        reverseString(string,stidx,i)
        
print string




