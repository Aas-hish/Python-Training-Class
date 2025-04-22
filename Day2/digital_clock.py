import time
import os

h=4
m=38
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
    
    
    
    
# for i,j,k in zip (range(1,50),range(99,50,-1),range(100,150,-1)):
#     print(i,end=" ")
#     print(j,end=" ")
#     print(k,end=" ")
#     print()