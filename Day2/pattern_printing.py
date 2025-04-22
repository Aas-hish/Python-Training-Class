n= int(input("Enter any number: "))

num = 1

for i in range(1, n+1):
    row = []
    
    for j in range(i):
        row.append(num)
        num += 1
    
    if i % 2 == 0:
        row.reverse()
    
   
    print('*'.join(map(str, row)))