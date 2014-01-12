
'''BalanceError is a subclass of the Exception class'''
class BalanceError(Exception):
    ''' The variable value is a class wide variable'''
    value = "Not enough funds. You have ${}."

from itertools import count;

class BankAccount:
    _ids = count(0);   
    def __init__(self,initAmount=0):
        self.balance = initAmount;
        self.accountId = BankAccount._ids.next();
        
    def getClassWideCount(self):
        return self._ids;
        
    def deposit(self, amount):
        self.balance +=amount;
        print "${} is deposited".format(amount);
    
    def withdraw(self, amount):
        if self.balance<amount:
            raise BalanceError, BalanceError.value.format(self.balance);
        else:
            self.balance-=amount;
            print "${} is withdrawn".format(amount);
    
    def showAccountId(self):
        return self.accountId; 
        
    def checkBalance(self):
        return self.balance;
    
    def transfer(self,amount, account):
        try:
            self.withdraw(amount)
            account.deposit(amount)
        except BalanceError:
            raise BalanceError, BalanceError.value.format(self.balance);
          
            
''' We want to create a specific kind of account. All the methods from BankAccount can be inherited. '''
class InterestAccount(BankAccount):
    def deposit(self,amount):
        BankAccount.deposit(self,amount)
        self.balance = self.balance * 1.03;
         
''' We want to create a chargingAccount that charges a withdrawal fee'''
class ChargingAccount(BankAccount):
        def __init__(self,initialAmount):
            BankAccount.__init__(self,initialAmount);
            self.fee = 2;
        
        def withdraw(self,amount):
            BankAccount.withdraw(self,amount+self.fee);
         