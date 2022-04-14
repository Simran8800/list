a=[1,2.3,"simi",1+2j,4,"mini"]
i=0
n={}
while i<len(a):
    n[a[i]]=type(a[i])
    i+=1
print(n)
    
    
        