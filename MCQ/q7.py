def love(a):
    if a> 8:
        return a
    print("PUSHPA")
    val = love(a+2)
    print("RRR")
    return val

for i in range(4,7):
    print("\n-----------------------")
    result = love(i)
    print(f"Returned value : {result}")