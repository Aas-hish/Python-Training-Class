def com_string(s):
    compressesd = ""
    count = 1
    for i in range(len(s)-1):
        if (s[i]==s[i+1]):
            count += 1
        else:
            compressesd = compressesd+ s[i] + str(count)
            count = 1
            
    compressesd = compressesd + s[-1] + str(count)
    print(compressesd)
            
            
s= input("Enter a string: ")
com_string(s)


