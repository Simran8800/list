# a=[2,-4,5,7,-6,-9,-7,6,8,-2,5]
# i=0
# b=[]
# while i<len(a):
#     if a[i]=="-":
#         b.append(a)
#     else:
#         b.append(a)
#     i=i+1
# print(b)
        

num=[50,40,70,56,26,58,45]
a=0
i=0
while i<len(num):
    if num[i]>a:
        a=num[i]
    i=i+1
i=0
b=0
while i<len(num):
    if num[i]>b:
        if num[i]!=a:
            b=num[i]
    i=i+1
print(b)
        

            
    



        

















