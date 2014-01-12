# regular expressions in Python

# . --> any character EXCEPT newline
# re.search('..g','uig').group() --> returns 'uig'
# but re.search('..g','uig').group() --> gives error. 

#  \d --> digit
#  \w -->  character: a letter or digit or underbar [a-zA-Z0-9_].
#  + --> one of more occurrences of the pattern to its left e.g. "i+" one or more i's
#  * --> zero or more occurrences of the pattern to its left
#  ? --> match 0 or 1 occurrences of the pattern to its left
#  \s --> white space
#  ^ ---> start of the string
#  $ ---> end of the string
# \s* --> one or more white spaces
# [] --> any set of characters in the list
# [^] --> any set of characters that are NOT in the list
# \D  --> matches any character except a numeric digit


# finding email addresses from a string
# str = 'purple alice@google.com, blah monkey bob@abc.com blah dishwasher'
# re.findall('[\w.-]+@[\w.-]+',str)

# we can also send an entire file through findall
# f=open('test.txt','r')
# re.findall(pattern, f.read())


# Extracting year from babynames

#names={}
#f= open('baby1990.html'); year = re.search('(Popularity in )(\d\d\d\d)',f.read()).group(2)
# f= open('baby1990.html'); list = re.findall('<td>(\d+)</td><td>([a-zA-z]+)</td><td>([a-zA-z]+)</td>',f.read());
#for t in list:
#    names[t[1]]=t[0]
#    names[t[2]]=t[0]

# snames = sorted(names.items(), key= lambda x: x[0]);
final =[year]
final= final+snames   
