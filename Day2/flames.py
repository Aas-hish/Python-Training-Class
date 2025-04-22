b_name = input("Boy name: ")
g_name = input("Girl Name: ")

l1 = list(b_name)
l2= list(g_name)

for i in range(len(l1)):
    for j in range(len(l2)):
        if l1[i] == l2[j]:
            l1[i] = '2'
            l2[j] = '2'
print(l1)
print(l2)
x = sum(1 for i in l1 if i != '2')
y = sum(1 for j in l2 if j != '2')
count = x + y


strr = "FLAMES"
ans= list(strr)
i =0
while (len(ans) !=1):
    i =(i+(count-1))%len(ans)
    ans.pop(i)
print(ans)

    



# Note ; to remove number from list
# a = [1,2,2,2,3,4,5]

# x =sum(1 for i in a if i!=2)
# print(x)
        