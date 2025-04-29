word ="HKNUDT"
for i in range(len(word)):
    for j in range(i+1):
        print(chr(ord(word[j]) +1),end=" ")
    print()