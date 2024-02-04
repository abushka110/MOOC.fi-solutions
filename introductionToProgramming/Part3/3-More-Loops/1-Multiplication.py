# solution 1
number = int(input("Please type in a number: "))

multiplier = 0
multiplicand = 0
product = 0

while multiplier < number:
    multiplier += 1
    while multiplicand < number:
        multiplicand += 1
        product = multiplier * multiplicand
        print(f"{multiplier} x {multiplicand} = {product}")
    multiplicand = 0

# solution 2
# number = int(input("Please type in a number: "))
# for multiplier in range(1, number + 1):
#     for multiplicand in range(1, number + 1):
#         product = multiplier * multiplicand
#         print(f"{multiplier} x {multiplicand} = {product}")
