a=[10,67,34,65]
b=[9,6,54,87,79]
c=[34,45,76,12,23]
a+=b+c
for i in range (0,len(a)):
    for j in range (i+1,len(a)):
        if (a[i]>a[j]):
            a[i],a[j]=a[j],a[i]
print(a)


