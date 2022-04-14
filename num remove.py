a=[1,0,2,3,0,5,0,6,7]
i=0
b=[]
while i<len(a):
    if a[i]!=0:
        b.append(a[i])
    i+=1
print(b)