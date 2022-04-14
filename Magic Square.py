magic_Square=[[8,3,4],
               [1,5,9],
               [6,7,2]]
row=0
row1=0
row2=0
column=0
column1=0
column2=0
diagonal1=0
diagonal2=0
i=0
while i<len(magic_Square):
    j=0
    while j<len(magic_Square[i]):
        if i==0:
            row+=magic_Square[i][j]
        elif i==1:
            row1+=magic_Square[i][j]
        elif i==2:
            row2+=magic_Square[i][j]
        j=j+1
    i=i+1
a=0
while a<len(magic_Square):
    k=0
    while k<len(magic_Square[a]):
        if k==0:
            column+=magic_Square[a][k]
        elif k==1:
            column1+=magic_Square[a][k]
        elif k==2:
            column2+=magic_Square[a][k]
        k=k+1
    a=a+1
b=0
while b<len(magic_Square):
    s=0
    while s<len(magic_Square[b]):
        if b==s:
            diagonal1+=magic_Square[b][s]
        if b+s==len(magic_Square[b])-1:
            diagonal2+=magic_Square[b][s]
        s+=1
    b=b+1

if row==row1==row2==column==column1==column2==diagonal1==diagonal2:
    print("row=",row)
    print("row1=",row1)
    print("row2=",row2)
    print("column=",column)
    print("column1=",column1)
    print("column2=",column2)
    print("diagonal1=",diagonal1)
    print("diagonal2=",diagonal2)
    print("It is a magic square.")
else:
    print("It isn't a magic square")
                
            
    


            
            
            
            
            
            
        








