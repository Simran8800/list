a=["simran"]
i=0
b=[]
while i<len(a):
    j=0
    x=5
    while j<len(a[i]):
        b.append(a[i][j])
        b.append(x)
        
        x=x+5
        j=j+1
    i+=1
print(b)