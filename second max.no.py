num=[50,40,23,70,56,19,15]
num.sort()
print(num)  #[15,19,23,40,50,56,70]

print("largest second number",num[-2])



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
print(b)