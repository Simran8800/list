elements = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
i=0
even=0
odd=0
while i<len(elements):
    sum=0
    sum=sum+elements[i]
    if sum%2==0:
        even+=sum
    else:
        odd+=sum
    i=i+1
print("total ave even no",even/i)
print("total ave odd no",odd/i)
    