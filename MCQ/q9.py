a = 5
b = 7
c = 12

# Find the maximum among a, b, and c
if a > b and a > c:
    num = a
elif b > a and b > c:
    num = b
else:
    num = c

# Counter for number of loops
count = 0

while True:
    count += 1 
    if num % a == 0 and num % b == 0 and num % c == 0:
        lcm = num
        break
    num += 1

print("LCM of", a, b, "and", c, "is", lcm)
print("Loop ran", count, "times.")
