# write to file
L = [ [5,6,7,8], [1,2,3,4,5] ];

f = open('jpt.txt','w')
# write each list in a row separated by a delimiter

delimiter=" "

for l in L:
    row = delimiter.join(str(x) for x in l)
    row = row+'\n'
    f.write(row)

f.close()



import json
A=[{'a':10,'b':5},{'a':44,'b':23}]
j = json.dumps(A)
f=open('writejson.json','w')
f.write(j)
f.close()


#write a json file 
listDict=[{"name":"anima","age":28},{"name":"anita","age":30}]
with open("myjson.json","w") as outfile:
    for j in listDict:
        json.dumps(j,outfile)
        outfile.write('\n')


f=open('myjson.json','r')
for l in f:
    data= json.loads(l)
    print data["name"]


# how to read a json file?

f=open('temp.json',r')

for line in f.readlines():
    data = json.loads(line)





