def trailing_zero(num):
    count = 0
    i = 5
    while num // i > 0:
        count += num // i
        i *= 5
    return count

print(trailing_zero(5))  

        
 