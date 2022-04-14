a=[1,1,0,1,1,1,0,1]
i=0
count=0
x=[]
while i<len(a):
    if a[i]>count:
        count=a[i]
    x.append(count)
    i=i+1
print(x)
    

