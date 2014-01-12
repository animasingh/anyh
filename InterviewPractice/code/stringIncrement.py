def stringSum(string1,string2):
    l1 = len(string1)
    l2 = len(string2)
    carry=0
    stringRes=''
    for i in range(1,max(l1,l2)+1,1):   
        if i<=l1 and i<=l2:
            #we have elements in both strings
            s=str(int(string1[-i])+int(string2[-i])+carry)
            
        elif i<=l1 and i>l2:
            #we have element in string1
            s = str(int(string1[-i]) + carry )
            
        elif i>l1 and i<=l2:
            # we have element in string2
            s = str(int(string2[-i])+carry)
          
        if len(s)==1:
           stringRes = s+ stringRes
           carry=0
        elif len(s)>1:
            stringRes = s[-1] + stringRes
            carry=1
        
    
    if carry==1:
        stringRes = '1'+stringRes        
    

    return stringRes


resNum = stringSum('109','99')
print resNum



def increment(strNum): 
	carry=1
	resNum=''
	
	for i in range(len(strNum)-1,-1,-1):
		if int(strNum[i])==9 and carry==1:
			resNum='0'+resNum
			carry=1
		elif int(strNum[i])<9 and carry==1:
			resNum = str(int(strNum[i])+1) + resNum
			carry=0
		else: 
			# if carry==0
			resNum = strNum[i] + resNum
	
	if carry==1:
		resNum = '1'+resNum
	
	return resNum

#resNum=increment('9')
#print resNum





