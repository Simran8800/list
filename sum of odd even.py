elements = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
i=0
even=0
odd=0
while i<len(elements):
    k=elements[i]
    if k%2==0:
        even+=k
    else:
        odd+=k
    i=i+1
print("total even no",even)
print("total odd no",odd)
    


