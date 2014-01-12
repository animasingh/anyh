def findPermutation(string):
    if len(string)==1:
        return [string]
        
    List=[]
    
    for i in range(0,len(string)):
        #print List
        L = findPermutation(''.join([string[:i],string[i+1:]]))
        #print string, i, string[i], L 
        L= [string[i]+c for c in L]
        #print L
        List.extend(L)
        #print List
    
    return List

import time

st = time.time()
res= findPermutation('abc')
print time.time()-st
#print res
#print len(res)


def permutations(string, step = 0):
    # if we've gotten to the end, print the permutation
    if step == len(string):
        print "".join(string)

    # everything to the right of step has not been swapped yet
    for i in range(step, len(string)):

        # copy the string (store as array)
        string_copy = [character for character in string]
        print step, i , string_copy
        # swap the current index with the step
        string_copy[step], string_copy[i] = string_copy[i], string_copy[step]
        print string_copy
        # recurse on the portion of the string that has not been swapped yet (now it's index will begin with step + 1)
        permutations(string_copy, step + 1)

st=time.time()
permutations('abc')
print time.time()-st