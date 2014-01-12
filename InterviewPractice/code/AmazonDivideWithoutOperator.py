# divide numbers without using "/" operator

def divide(number,divisor):
    
    if number<0 and divisor<0:
        sign=1
    elif divisor<0:
        sign=-1
    elif number<0:
        sign=-1
    quotient=0
    while number>=divisor:
        number = number-divisor
        quotient=quotient+1
    
    return quotient*sign
    
    
    
