
passs = input("Enter passwaord:")
dg=0
up=0
sp=0
sm=0

if (len(passs)>7):
    for i in passs:
        if(i.isupper()):
            up=up+1
        elif(i.islower()):
            sm= sm+1
        elif(i.isdigit()):
            dg=dg+1
        else:
            sp=sp+1
            
    if(up>0 and sm>0 and dg>0 and sp>0 ):
        print("Strong Password")
    else:
        print("Weak Password")
else:
    print("Need to alteast 8 character")