# Author: Ryan (AMDG) 10/1/21

a = int(input("Team 1, # of wins: "))
b = int(input("Team 1, # of ties: "))
c = int(input("Team 2, # of wins: "))
d = int(input("Team 2, # of ties: "))

if a + b > c + d:
    print("Team 1 wins")
elif c + d > a + b:
    print("Team 2 wins")
else:
    print("It was a tie")
