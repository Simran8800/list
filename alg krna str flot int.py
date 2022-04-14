a=[2,3,4.0,4.3,6,7,8.3,"kiti","kirtee",6,7.8] 
i=0
b=[]
c=[]
d=[]
while i<len(a):
    if type(a[i])==int:
        b.append(a[i])
    if type(a[i])==str:
        c.append(a[i])
    if type(a[i])==float:
        d.append(a[i])          
    i=i+1
print(b)
print(c)
print(d)
        
        

        
        
       