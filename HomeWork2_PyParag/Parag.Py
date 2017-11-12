import re
MyFile=open('paragraph_2.txt','r')
count=0
given_words=[]
for x in MyFile.read().split():
    count+=1
    if x in given_words:
        words.setdefault(x,0)
        words[str(x)]+=1    
print(" Approximate Word Count : " + str(count))






