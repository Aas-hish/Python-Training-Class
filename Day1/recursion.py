# def flower(a):
#     if(a==4):
#         return 
#     print(a+10,end=" ")
#     flower(a+1)
#     print(a,end=" ")

# flower(1)

# def raju(a):
#     if(a==1):
#         return
#     a =a-1
#     raju(a)
#     print("Hai")
#     raju(a)
    
    
# raju(5)



# def abc(a):
#     if a==4:
#         return
#     a = a + 1
#     abc(a)
#     print("CSE"  ,end=" ")
#     abc(a)
#     print("MECH ",end=" ")
    
# def main():
#     num = "12"
#     for a in num:
#         print()
#         abc(int(a))
        
# main()


def abc(n):
    if n==1:
        return 2
    b = abc(n-1)
    print("hai",end=" ")
    return b + 1

print(abc(5))
        