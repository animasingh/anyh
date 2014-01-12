def simple_generator_function():
    yield 1
    yield 2
    yield 3
    
for v in simple_generator_function():
    print v;
    

def is_prime(number):
    if number>1:
        if number==2: #if the number is 2, it is prime
            return True
        if number % 2 ==0: # any other even number is NOT a prime
            return False
        for current in range(3,int(math.sqrt(number)+1),2):
            if number % current ==0:
                return False
        return True
    return False


def get_primes(number):
    while True: #this line allows us to get_primes on an infinite list
        if is_prime(number):
            yield number
        number=number+1;
        
def solve_number_10():# here we are trying to find the sum of all prime numbers below 2,000,000 (2 million)
    total=2
    for next_prime in get_primes(3):
        if next_prime<2000000:
            total+=next_prime
        else:
            print(total)
            return
# we can also send stuff to generators. 
def print_successive_primes(iterations, base=10):
    prime_generator = get_primes(base)
    prime_generator.send(None)
    for power in range(iterations):
        print(prime_generator.send(base ** power))
        
def get_primes(number):
    while True:
        if is_prime(number):
            number = yield number
        number += 1
        


    