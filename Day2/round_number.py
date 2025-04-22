def isround(n):
    res=[]
    
    while (n!=1):
        if(n in res):
            return False
        res.append(n)
        n=sum(int(digit) *int(digit) for digit in str(n)) 
    return True

print(isround(19)) 
print(isround(2))
print(isround(10))





