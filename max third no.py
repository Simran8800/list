num=[50,40,70,56,26,58,45]
a=0
i=0
while i<len(num):
    if num[i]>a:
        a=num[i]
    i=i+1
i=0
b=0
while i<len(num):
    if num[i]>b:
        if num[i]!=a:
            b=num[i]
    i=i+1
i=0
c=0
while i<len(num):
    if num[i]>c:
        if num[i]!=b and num[i]!=a:
            c=num[i]
    i=i+1
print(c) 

