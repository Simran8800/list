a=[6,7,8,[5,6,7],[6,7,8]]
sum=0
i=0
while i<len(a):
    if type(a[i])==list:
        pass
    else:
        sum=sum+a[i]
    i=i+1
print(sum)
       