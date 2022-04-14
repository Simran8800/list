a= [4, 6, 4, 3, 3, 4, 3, 4, 3, 8]
b=[]
c=[]
d=[]
i=0
while i<len(a):
    if a[i] not in b:
        b.append(a[i])
    else:
        c.append(a[i])
    i+=1
j=0
while j<len(c):
    if c[j] not in d:
        d.append(c[j])
    j+=1
print(d)



    
