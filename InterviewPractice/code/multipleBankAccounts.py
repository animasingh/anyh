''' Create many bank accounts'''

from BankAccount import *;
import time;

def getNextId():
    a=raw_input('Create account[y/n]?');
    if a[0] in 'yY':
        id = time.time();
        id = int(id) % 10000;
    else:
        id=-1;
    return id


accounts={} ; '''Dictionary'''
while 1:
    id = getNextId();
    if id ==-1:
        break;
    bal = float(raw_input('Opening Balance?'));
    accounts[id]=BankAccount(bal);

for id in accounts.keys():
    print 'AccountId:{0}, Balance:{1},'.format(id, accounts[id].checkBalance());
    

