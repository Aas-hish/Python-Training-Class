#random game

import time
import random
name1=input("Enter the player1:")
name2=input("Enter the player2:")
print("Computer has fixed 5 number of integers in its mind")
print("You both have three turns each to guess it")
print("Ready for the game?")
nums=[]
while(len(nums)<5):
    ran=random.randint(1,10)
    if ran not in nums:
        nums.append(ran)
print(nums)
player1=[]
player2=[]
s1=0
s2=0
for i in range(3):
    print("Hii {} Guess your Number {}".format(name1,i+1))
    x=int(input())
    while(x in player1 or x in player2):
        print("Already choosen, so choose another number:")
        x=int(input())
    player1.append(x)
    if x in nums:
        print("CORRECT!")
        s1=s1+1
    else:
        print("WRONG")
    print("Hii {} Guess your Number {}".format(name2,i+1))
    x=int(input())
    while(x in player1 or x in player2):
        print("Already choosen, so choose another number:")
        x=int(input())
    player2.append(x)
    if x in nums:
        print("CORRECT!")
        s2=s2+1
    else:
        print("WRONG")
print("---------------------------------")
print("Lets have summary")
print("Computer has choosen: {}".format(nums))
print("{} has choosen {}".format(name1, player1))
print(f"{name1} score is {s1}")
print("{} has choosen {}".format(name2, player2))
print(f"{name2} score is {s2}")
if s1<s2:
    print("{} has won the game with score {}".format(name2, s2))
elif(s1>s2):
    print("{} has won the game with score {}".format(name1, s1))
elif(s1==s2):
    print("------->DRAWN<-------")