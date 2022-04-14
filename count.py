a=[1,2,3,[],[],4,5,[7,8]]
i=0
b=[]
while i<int(len(a)):
  while i<(len(a)):
        j=0
        n=[]
        count=0
        while j<int(len(a)):
            while j<(len(a)):
                if a[i]==a[j]:
                    if a[i]==a[j]:
                        count=count+1
                        print()
                j=j+1
        n.append(a[i])
        n.append(count)
        if n not in b:
            b.append(n)
        i=i+1
print(b)
            
            








            