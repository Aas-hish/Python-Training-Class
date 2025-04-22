def percentage(person):
    total = sum(person["marks"])
    return total/len(person["marks"])
a = [
    {"name":"raju","age":23, "marks":[40,45,80,75]},
    {"name":"Ram","age":24, "marks":[50,55,60,50]},
    {"name":"Ravi","age":22, "marks":[70,65,85,70]},
    {"name":"Jack","age":21, "marks":[70,40,90,60]}
]

b= sorted(a,key=percentage,reverse=True)
print(b)
position = ["first", "second", "third", "fourth"]
pos=0
for i in b:
    print("{} has score {} % ---> stands {}".format(i["name"],percentage(i),position[pos]))
    pos =pos+1



n = int(input("Enter number of rows: "))
num = 1

for i in range(1, n + 1):
    row = []

    for j in range(i):
        row.append(num)
        num += 1

    if i % 2 == 0:
        row.reverse()

    print('*'.join(map(str, row)))

