



class myClass:
    """Simple example"""
    i=1234
    
    def __init__(self):
        self.data=[];
        
    def f(self):
        return "hello world"
        
    def set_data(self, list):
        self.data= list;
        
        
        
        
        
        
x=myClass()


class Reverse:
    i=3 #class variable or static variable. They can be accessed 
    def __init__(self, data):
        self.data = data; 
        self._index = len(data)
    
    def __iter__(self):
        return self
    
    def next(self):
        if self._index==0:
            raise StopIteration
        self._index=self._index-1
        return self.data[self._index]
        



class Paranoid(object):
    def __init__(self):
        self._secret = 0

    def set(self, val):
        self._secret = val * 10

    def get(self):
        return self._secret / 10

p = Paranoid()
p.set(123)
print p.get() # 123
print p._secret # 1


