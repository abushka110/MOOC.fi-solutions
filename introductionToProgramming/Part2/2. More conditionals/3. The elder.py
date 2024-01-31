print("Person 1: ")
personOneName = input("Name: ")
personOneAge = int(input("Age: "))

print("Person 2: ")
personTwoName = input("Name: ")
personTwoAge = int(input("Age: "))

if personOneAge < personTwoAge:
    print(f"The elder is {personTwoName}")
elif personOneAge > personTwoAge:
    print(f"The elder is {personOneName}")
else:
    print(f"{personOneName} and {personTwoName} are the same age")