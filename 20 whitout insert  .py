s=[65,23,45,65,43,87,21,90,99,12,32,53]
i=0
a=[]
count=1
while i<len(s):
    a.append(s[i])
    if count==4:
        a.append(20)
        count=0
    count+=1
    i=i+1
print(a)
    
    