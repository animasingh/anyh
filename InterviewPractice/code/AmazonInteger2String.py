def integer2string(integer):
    MAXDIGITS=10
    stringlist = [0] * MAXDIGITS
    counter=0
    negativeFlag=0
    if integer<0:
        integer=abs(integer)
        negativeFlag=1
    if integer==0:
        return '0'
    
    while integer>0:
        digit = integer % 10 
        integer = integer / 10 
        # stringlist contains the digit in a reverse order
        stringlist[counter]= chr(ord('0') + digit)
        counter+=1
    
    if negativeFlag==1:
        stringlist[counter]='-'
        counter+=1
    
    print stringlist    
    return ''.join(  [ stringlist[i] for i in range(counter-1,-1,-1)]    )

    
    

print integer2string(-1)
print integer2string(0)
print integer2string(1)