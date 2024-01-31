numOne = int(input("Please type in the first number: "))
numTwo = int(input("Please type in another number: "))
if numOne < numTwo:
    print(f"The greater number was: {numTwo}")
elif numOne > numTwo:
    print(f"The greater number was: {numOne}")
else:
    print("The numbers are equal!")