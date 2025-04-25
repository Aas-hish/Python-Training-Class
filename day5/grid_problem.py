import random as r


def generate_grid(rows,cols):
    if rows<3 or cols<3:
        print("Not possible")
        return
    
    while True:
        g = [[r.randint(1, 99) for _ in range(cols)] for _ in range(rows)]
        outer_sum = 0
        inner_sum = 0

        for i in range(rows):
            for j in range(cols):
                if i == 0 or i == rows - 1 or j == 0 or j == cols - 1:
                    outer_sum += g[i][j]
                else:
                    inner_sum += g[i][j]
                    
        if outer_sum==inner_sum:
            print("\nBalanced Grid")
            for row in g:
                print(row)
            print("\nOuter Sum:", outer_sum)
            print("Inner Sum:", inner_sum)
            break

rows= int(input("Enter number of row: "))
cols= int(input("Enter number of cols: "))
generate_grid(rows,cols)

    


    