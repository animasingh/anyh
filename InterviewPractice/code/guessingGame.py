def check_guess(x): 
     secret_number = -10; 
     if x<secret_number: 
               return -1
     elif x>secret_number: 
               return 1
     elif x==secret_number: 
               return 0

import random

def guessing_game(lower_limit,  upper_limit):
    guess =( lower_limit +upper_limit)/2
    #guess = random.randint(lower_limit, upper_limit)
    #print guess 
    # check if the guess is correct
    if check_guess(guess) ==0:
        print guess
    elif check_guess(guess)==-1:
        guessing_game(guess, upper_limit)     
    elif check_guess(guess)==1:
        guessing_game(lower_limit, guess)

import time
t0=time.time()
guessing_game(-500000,500000)
print time.time()-t0