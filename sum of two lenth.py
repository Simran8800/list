a=[[6,7,5,3],[5,6,3]] 
b=[[4,5,2,6],[6,7,4]] 
i=0
d=[]    
while i<len(a):
    j=0
    while j<len(a[i]):
        sum=a[i][j]+b[i][j] 
        d.append(sum) 
        j=j+1
    i=i+1
print(d)    
     