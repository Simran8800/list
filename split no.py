a=int(input("enter the no"))
i=0
while i<a:
    sum=a%10
    b=a-sum
    c=(b%100)
    d=a-c-sum
    i=i+1
print(d,"+",c,"+",sum)
                

