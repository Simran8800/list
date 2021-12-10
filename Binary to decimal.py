Binary=[1,0,0,1,1,0,1,1]
i=0
sum=0
while i<len(Binary):
    a=Binary[-1-i]
    sum=sum+a*(2**i)
    i=i+1
print(float(sum))