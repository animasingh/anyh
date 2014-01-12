# -*- coding: utf-8 -*-
# implement hash table in python

class keyValue:
    def __init__(self,key,value):
        self.key = key
        self.value = value
    def getKey(self):
        return self.key
    def getValue(self):
        return self.value


class hashTable:
    tablesize=20
    def __init__(self):
        self.list=[0]*hashTable.tablesize
        
    def hashFunction(self,key):
        # assuming that they key is string
        hashCode=1;
        for c in key:
            hashCode = 101*hashCode + ord(c);
            
        return hashCode;
    
    def get(self,key):
        
        # compute hash code that corresponds to the key
        hashCode = self.hashFunction(key)       
        # convert hash code to an index
        index= hashCode % hashTable.tablesize
        
        if self.list[index]==0:
            return "Key does not exist!"
        else:
            for kv in self.list[index]:
                if kv.getKey()==key:
                    return kv.getKey(), kv.getValue()
            return "Key does not exist"

            
        # if it is not empty return value
        return 
        
    def set(self,key,value):     
        # compute hash code that corresponds to the key
        hashCode = self.hashFunction(key)  
        print hashCode     
        # convert hash code to an index
        index= hashCode % hashTable.tablesize
        print index
        #check for collisons
        if self.list[index]==0:
            # set the corresponding index to a keyValue pair
            self.list[index] = [keyValue(key,value)]
        else:
            self.list[index].append(keyValue(key,value))
        
 