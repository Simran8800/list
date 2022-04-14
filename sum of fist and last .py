x=[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
i=0
sum=0
while i <len(x):
    j=0
    while j<len(x[i]):
        if i==0:
            sum+=x[i][j]
            if j>=1:
                sum+=x[i][2]
        j+=1
    i+=1
print(sum)