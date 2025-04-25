import random as r

rows, cols = 4,5
g = [[r.randint(1, 20) for _ in range(cols)] for _ in range(rows)]

for row in g:
    print(row)