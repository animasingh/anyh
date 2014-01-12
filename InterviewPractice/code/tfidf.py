#write code to compute tfidf for each word in each document in the given folder

from collections import defaultdict
import json
from operator import itemgetter
import math

tf = defaultdict(int) #key: (reviewId,word); value: # of times a word appears in the review
df = defaultdict(list) # key:word ; value: list of reviewId the word appears in

f = open('../data/yelpSample.json','r')
numDocs=0
for line in f:
    data = json.loads(line)
    review= data["text"]
    words = review.split()
    reviewId = data["review_id"]
    
    for word in words:
        tf[(reviewId,word)]+=1
        
        if reviewId not in df[word]:
            df[word].append(reviewId)
    numDocs+=1
           
#sort tf by count (ie which word appears the most in one review)
stf = sorted(tf.items(), key=itemgetter(1), reverse=True)

stf = sorted(tf, key = lambda x: tf[x], reverse=True)

#sort df (which word appears in the most reviews)
sdf = sorted(df, key=(lambda k: len(df[k])),reverse=True)

tfidf = defaultdict(int)

for review_word_pair in tf:
    #compute tfidf
    word = review_word_pair[1]
    tfidf[review_word_pair] = tf[review_word_pair] * math.log(numDocs*1.0/len(df[word]))

f.close()
        
        
import os
a = os.listdir('~/Documents/Python/code');

        
    
    
    
    
    
    
    








