a=[[2,3],[4,5,3,5],[5],[4,5,6,7,6,8,9]]
i=0
while i<len(a):
    j=0
    while len(a[j])<len(a[i]):
       j=j+1
    i=i+1
print("max lenth =",len(a[j]),a[j])


 