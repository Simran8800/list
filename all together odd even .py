elements = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
i=0
even=0
odd=0
while i<len(elements):
    k=elements[i]
    sum=0
    sum=sum+k
    if k%2==0:
        print("total even no",k)
        even+=sum
    else:
        print("total odd no",k)
        odd+=sum
    i=i+1
print("total ave even no",even/i)
print("total ave odd no",odd/i)
print("total sum even no",even)
print("total sum odd no",odd)
    
    

    
 
    
    
    
    
    
    
    
    
    
    
    
    
    



































