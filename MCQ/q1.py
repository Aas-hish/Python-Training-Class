a=3
i=1
while i<7:
    i=i+1
    if i==3 or i==6:
        continue
    for j in range(1,i+1):
        a +=1
    a +=2
print(a)
    