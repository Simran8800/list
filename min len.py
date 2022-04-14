num=[[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]]
i=num[0]
a=0
while a<len(num):
    if num[a]<i:
        i=num[a]
    a=a+1
print("lenth = ",len(i),i)