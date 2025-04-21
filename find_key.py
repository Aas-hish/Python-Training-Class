def max_digit(n):
    return max([int(d) for d in str(n)])

def min_digit(n):
    return min([int(d) for d in str(n)])

input1 = int(input("Enter 1st input: "))
input2 = int(input("Enter 2nd input: "))
input3 = int(input("Enter 3rd input: "))

largest = max_digit(input1) + max_digit(input2) + max_digit(input3)
smallest = min_digit(input1) + min_digit(input2) + min_digit(input3)

print("Sum of largest + smallest digits:", largest + smallest)
