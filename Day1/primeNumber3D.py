def is_prime(a):
    if a < 2:
        return False
    for i in range(2, int(a**0.5) + 1):
        if a % i == 0:
            return False
    return True

def sum_digit(a):
    return sum([int(i) for i in str(a)])

def tot_digit(a):
    return len(str(a))

n = int(input("Enter any number: "))
res = []
a = 1
while a < n:
    if is_prime(a):
        s = sum_digit(a)
        total = tot_digit(a)
        if is_prime(s) and is_prime(total):
            res.append(a)
    a += 1

print("Result:", res)
