# Author: Ryan (AMDG) 10/1/21

x = int(input("Input #: "))

if x % 2 == 0 and x % 3 == 0 and x % 5 == 0:
    print("multiples of 2, 3 and 5")
elif x % 2 == 0 and x % 3 == 0:
    print("multiples of 2 and 3")
elif x % 2 == 0 and x % 5 == 0:
    print("multiples of 2 and 5")
elif x % 3 == 0 and x % 5 == 0:
    print("multiples of 3 and 5")
elif x % 2 == 0:
    print("multiple of 2")
elif x % 3 == 0:
    print("multiple of 3")
elif x % 5 == 0:
    print("multiple of 5")
