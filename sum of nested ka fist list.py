a=[[2,4,5],[5,4,3],[4,5,4]]
i=0
sum=0
while i<len(a):
    j=0
    while j<len(a[i]):
        sum=sum+a[i][j]
        
        j+=1
        break
    i+=1
print(sum)

