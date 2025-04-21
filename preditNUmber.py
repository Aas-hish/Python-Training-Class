list = [1,2,2,3,4,4,4,5,6]
u = set(list)
for num in u:
    if num % 2==0:
        list.remove(num)
        
print(list)