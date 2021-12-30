a=[1,-2,3,-4,5,-6,-7,-8]
b=[]
i=0
while i<len(a):
    if a[i]<=0:
        b.append(0)
    else:
        b.append(a[i])
    i=i+1
print(b)


