import time
import os

h=3 
m=3
s=0
while True:

    print("{:02d}:{:02d}:{:02d}".format(h,m,s))
    time.sleep(1)
    s=s+1
    if(s==60):
        s=0
        m=m+1
    elif(m==60):
        m=0
        h=h+1
    elif(h==12):
        s=0
        m=0
        h=0
    os.system("clear")