from math import sqrt

num = float(input("Please type in a number: "))

while num != 0:
    if num < 0:
        print("Invalid number")
    else:
        print(sqrt(num))
    num = float(input("Please type in a number: "))
else:
    print("Exiting...")