#given a list of numbers and a number. Check if there are two numbers in the list that adds up to the NUMBER

def checkSum(List,Number):
    List.sort() #O(n*log(n))
    # now perform a binary search on the sorted list
    for idx,item in enumerate(List):
        delta = Number-item
        if delta>List[-1]:
            continue
        else:
            if binarySearch(List[idx+1:],delta):
                return True
    return False
        
        
# implement binary search of a list --> O (logn)
def binarySearch(sortedlist, Number):
    if len(sortedlist)==0:
        return False
    else:
        if sortedlist[0]==Number or sortedlist[-1]==Number:
            return True
        else:
            mid = len(sortedlist)/2
            if Number==sortedlist[mid]:
                return True
            elif Number<sortedlist[mid]:
                return binarySearch(sortedlist[0:mid],Number)
            elif Number>sortedlist[mid]:
                return binarySearch(sortedlist[mid+1:],Number)
   
                            
L=[3,1,6,4,5]
Number=12                                                                              
print checkSum(L,Number)             
            