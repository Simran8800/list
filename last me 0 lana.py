a=[1,0,2,3,0,5,0,6,7]
c=[]
b=[]
for i in a:
    if i==0:
        c.append(i)
    else:
        b.append(i)
print(b+c)