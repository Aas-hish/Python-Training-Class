def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

a = int(input("Enter any number: "))

for i in range(5, a + 1):  
    for j in range(4, i): 
        for k in range(3, j):  
            if k * k + j * j == i * i:  
                if gcd(gcd(i, j), k) == 1:  
                    print(i, j, k)