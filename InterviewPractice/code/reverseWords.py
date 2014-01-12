sentence = "My name is Anima"

# Using the python split option
words = sentence.split();
reverse_sentence='';
for i in range(len(words)-1,-1,-1):
    reverse_sentence+=' '+words[i];
  
print reverse_sentence[1:]


# without using the python split option
reverse_sentence='';
numletters=0;

for i in range(len(sentence)-1,-1,-1):
    numletters+=1;
    
    if i==0:
        reverse_sentence+=' '+ sentence[i:i+numletters];
        numletters=0;
    elif sentence[i]==' ':
        reverse_sentence+=' '+ sentence[i+1:i+numletters];
        numletters=0;
    
        
print reverse_sentence;