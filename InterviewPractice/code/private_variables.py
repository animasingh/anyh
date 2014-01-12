class Critter(object):
    def __init__(self,name, mood):
        self.name = name; # public
        self.__mood = mood; #private
        
    def talk(self):
        print "I'm {0}".format(self.name)
        print "I feel {0}".format(self.__mood)
    
    def __private_method(self):
        print 'This is a private method'
    
    def public_method(self):
        print "This is a public method"
        self.__private_method()
    
    def __lt__(self,other):
        return self.name<other.name
        
        
        
        
c = Critter('anima','tired');
# to access a private function we have to do the following:
c._Critter__private_method()

#If we do the following, we will get an error:
#c.private_method()
#c.__private_method()

# we can access public variable
c.name
# we can also set public variable
c.name = 'anisha'

# we cannot access private variable like below
#c.mood 

#if we want to access private variable/attribute
c._Critter__mood

                
# this uses private variable          
class BankAccount(object):
    def __init__(self,amount=0):
        self.__value=amount; #private
    
    def deposit(self,amount):
        self.__value=self.__value+amount;
    
    def showBalance(self):
        return self.__value
        
b = BankAccount(10000);
b.showBalance();
b.value=0
b.showBalance(); # will still be 10000. 

# this class simply uses public variable        
class BankAccount(object):
    def __init__(self,amount=0):
        self.value=amount; #public 
    
    def deposit(self,amount):
        self.value=self.value+amount;
    
    def showBalance(self):
        return self.value
b = BankAccount(10000);
b.showBalance();
b.value=0
b.showBalance(); # the value will be 0. 