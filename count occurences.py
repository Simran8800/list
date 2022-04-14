char_list = ["a", "n", "t", "a", "a", "t", "n", "n", "a", "x", "u", "g", "a", "x", "a"]
i=0
a=[]
while i<len(char_list):
    j=0
    b=[]
    count=0
    while j<len(char_list):
        if char_list[i] in char_list:
            if char_list[i]==char_list[j]:
               count=count+1
               print()
        j=j+1
    b.append(char_list[i])
    b.append(count)
    if b not in a:
       a.append(b)
    i+=1
print(a)    
        
    
# a=[1,2,"apple","banana",4,5]
# i=0
# b=[]
# while i<int(len(a)):
#   while i<(len(a)):
#         j=0
#         n=[]
#         count=0
#         while j<int(len(a)):
#             while j<(len(a)):
#                 if a[i]==a[j]:
#                     if a[i]==a[j]:
#                         count=count+1
#                         print()
#                 j=j+1
#         n.append(a[i])
#         n.append(count)
#         if n not in b:
#             b.append(n)
#         i=i+1
# print(b)
            
                
        