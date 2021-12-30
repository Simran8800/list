n = [19, 17, 12, 17, 17, 18, 10, 17, 14, 12, 19, 17, 12, 13, 11]
print("list before",n)
d=[]
for i in n:
    if i not in d:
        d.append(i)
n=d
print("list after removing duplicates",n)

    