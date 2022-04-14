a=[12,345,23,22]
i=0
b=[]
while i<len(a):
    sum=0
    while a[i]>0:
        sum=sum+a[i]%10
        a[i]//=10
    b.append(sum)
    i+=1
print(b)
