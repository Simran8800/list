a=[7,4,[5,4],[4,3],54,5]
i=0
sum=0
while i<len(a):
     if type(a[i])==list:
        j=0
        while j<len(a[i]):
            sum=sum+a[i][j]
            j=j+1
     else:
          sum=sum+a[i]
     i=i+1
print(sum)
          

    
    