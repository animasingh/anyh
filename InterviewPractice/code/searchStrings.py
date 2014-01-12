string='animaz'; 
letters={}; # intialize a dictionary. keys:distinct letters in the string and values: corresponding idx
idx=0;
for item in string: 
    if item not in letters:
        letters[item]=idx;
        idx+=1;
        
bitArray = [0] * len(letters);

sumVAR=0; # keeps track of how many distinct letters in string are identified so far.
document = 'this is a documentz hello hello hello hello';

for pos, s in enumerate(document):
    if sumVAR==len(letters):
        print pos-1, len(document);
        break
           
    if s in letters:
        if bitArray[letters[s]]==0: # we are seeing the letter fo the first time
            bitArray[letters[s]]=1;
            sumVAR+=1;
            

if sumVAR==len(letters):
    print "All letters found!";
else:
    print "All letters not found.";
    