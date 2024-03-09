# print beginning sum
sum = 0
print(sum)

while True:
    # ask user for input
    calculation = input("Type in a calculation or quit: ")

    # check if user want to quit
    if calculation == "quit":
        break

    # split calculation operator and calculation number
    calculation_type = calculation[0]
    num = calculation[1:]

    # make the calculation
    if calculation_type == "-":
        sum -= int(num)
    elif calculation_type == "+":
        sum += int(num)

    # print sum of calculation
    print(sum)
    