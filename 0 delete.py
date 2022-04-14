num=[101,120,1201]
i=0
b=[]
while i<len(num):
    j=str(num[i])
    k=0
    s=''
    while k<len(j):
        if j[k]!='0':
            s+=j[k]
            b.append(int(s))
        k+=1
    i+=1
print(b)

