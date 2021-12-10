num=[50,40,23,70,56,19,15,]
i=num[0]
a=0
while a<len(num):
    if num[a]>i:
        i=num[a]
    a=a+1
print(i)        



a=[]
size=int(input('enter the size of list'))
for i in range(size):
    val=int(input("enter number"))    
    a.append(val)
max=a[0]
for i in range(size):
    if(a[i]>max):
        max=a[i]
print("max number=",max)
    