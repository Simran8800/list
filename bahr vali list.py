a=[6,7,8,[5,6,7],[6,7,8]]
sum=0
i=0
b=[]
while i<len(a):
    if type(a[i])==list:
        pass
    else:
        b.append(a[i])
        sum=sum+a[i]
    i=i+1
print(b)
        
       