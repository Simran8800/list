list=[1,2,3,4,5,6,7,8]
list2=[2,4,6,8,10]
length=len(list)
length2=len(list2)
b=[]
c=[]
for i in range(length):
    diff=1+list[i]-list[i]
    b.append(diff)
print(b)
for j in range (length2):
    diff1=2+list2[j]-list2[j]
    c.append(diff1)
print(c)
    
    
    

