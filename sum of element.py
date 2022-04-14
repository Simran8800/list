l=[256,26,14,2]
c=[]
i=0
while i<len(l):
    sum=0
    while l[i]>0:
        sum=sum+l[i]%10
        l[i]//=10
    c.append(sum)
    i=i+1
print(c)
    
    
# a=int(input("enter the number"))
# i=0
# while i<len(a[i]):
#     sum=0
#     while a[i]>0:
#         sum=sum+a[i]%10
#         a[i]//=10
#     i=i+1
# print(sum)