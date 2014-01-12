''' Introduction to OOP'''

'''Convention to name a class beginning with a capital letter'''
class Message:
    def __init__(self,astring):
        self.text = astring;
    def printIt(self):
        print self.text; 
        
'''Polymorphism'''
class Square:
    def __init__(self,side):
        self.side = side;
    def calculateArea(self):
        return self.side*self.side; 
        
class Circle:
    def __init__(self,radius):
        self.radius=radius;
    
    def calculateArea(self):
        import math;
        return math.pi*self.radius**2;

class BalanceError(Exception):
    value = "Not enough funds. You only have ${}"
class BankAccount:
    def __init__(self,initAmount):
        self.balance = initAmount;
        
    def deposit(self, amount):
        self.balance +=amount;
        print "${} is deposited".format(amount);
    
    def withdraw(self, amount):
        if self.balance<amount:
            raise BalanceError.format(self.balance)
        else:
            self.balance-=amount;
            print "${} is withdrawn".format(amount);
        
        
        