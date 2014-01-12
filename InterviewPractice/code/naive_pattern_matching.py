
# naive string matching algorithm

t = 'this is a sentence with anima and anisha in it';
p = 'sentence';

for i in range(0,len(t)-len(p)):
    if t[i:i+len(p)] == p:
        print "Pattern found at", i;
        break
        