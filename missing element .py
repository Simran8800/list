a=[1,2,5,6,8,10]
i=1
b=[]
c=max(a)
while i<c:
    if c>=i:
       if i not in a:
           b.append(i)
    i=i+1
print(b)

