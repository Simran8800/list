kitna_paisa_hai = [3000, 600000, 324990909, 90990900, 30000, 5600000, 690909090, 31010101, 
                   532010, 510, 4100]
i=0
carorpati=0
lakhpati=0
dilwala=0
while i<len(kitna_paisa_hai):
    if kitna_paisa_hai[i]>100000000:
        carorpati+=1
    elif kitna_paisa_hai[i]>1000000:
        lakhpati+=1
    else:
        dilwala+=1
    i=i+1
print("crorpati",carorpati)
print("lakhpati",lakhpati)
print("dilwala",dilwala)