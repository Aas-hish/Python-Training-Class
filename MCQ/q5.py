def result(a, k):
    c = 2
    if all(a):
        c = c + 1
    elif any(a):
        c = c - 2
    a.pop()
    a.append(c)
    if all(a[-2:]):
        return k + 2
    return k

a = [1, 2, 3, 1, 4, 1, 3, 13, 99, 0, 9]
print(result(a, 3))
