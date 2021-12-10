list1 = [1,2,3,4,5,6]
list2 = [2,3,1,0,6,7]
j=[]
i=0
while i<len(list1):
    k=list1[i]
    if k not in list2:
        j.append(k)
    i=i+1
print(j)