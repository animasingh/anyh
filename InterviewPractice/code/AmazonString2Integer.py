def string2integer(string):
    integer=0
    if string[0]=='-':
        multiplier=-1
        stidx=1
    else:
        multiplier=1
        stidx=0
    #print stidx
    significance=1
    for i in range(len(string)-1,stidx-1,-1):
        #print string[i]
        #print ord(string[i])-ord('0')   
        integer = integer + (ord(string[i])-ord('0')) * significance
        #print integer
        significance= significance*10
    
    return integer*multiplier
    
string='-123'
print string2integer(string)

string ='98'
print string2integer(string)

string = '0'
print string2integer(string)