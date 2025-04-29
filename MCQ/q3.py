c=0
for i in range(3):
    for j in range(4):
        if j==i:
            break
        c +=1
        for k in range(4):
            if k==j:
                break
            c +=1
        
print(c)