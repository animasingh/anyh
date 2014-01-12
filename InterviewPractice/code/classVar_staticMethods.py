# static methods and class attributes

class Critter(object):
    __total=0; # class attribute
    
    def status():
        print "The number of critters is: {0}".format(Critter.__total)
    status = staticmethod(status) # declaring that this is a static method. Note that since this is a static method, we do not need to pass self as an argument. 
    
    def __init__(self,name):
        self.name = name; # public
        Critter.__total+=1;
        
    def talk(self):
        print "I'm {0}".format(self.name)

    def __str__(self):
        return "I am a Critter object. Name: {0}".format(self.name);
        
    
  

print Critter._Critter__total
c = Critter('aba');
g = Critter('aja');

Critter.status()
print "Accessing the class attribute through an object"
print c.total

#class attributes
#static methods: associated with a class attributes. 
