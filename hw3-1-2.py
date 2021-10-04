# Author: Ryan (AMDG) 10/1/21

x = int(input("Input first card's worth: "))
y = int(input("Input second card's worth: "))

if x + y <= 21:
    print("Safe")
else:
    print("Bust!")
