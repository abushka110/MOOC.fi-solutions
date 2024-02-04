num = int(input("Please type in a number: "))

while num > 0:
    multiplicand = 1
    factorial = 1
    while multiplicand < num:
        multiplicand += 1
        factorial *= multiplicand
    print(f"The factorial of the number {num} is {factorial}")
    num = int(input("Please type in a number: "))

print("Thanks and bye!")