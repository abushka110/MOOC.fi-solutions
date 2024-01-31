letterOne = input("1st letter: ")
letterTwo = input("2nd letter: ")
letterThree = input("3rd letter: ")

if letterOne > letterTwo and letterOne < letterThree or letterOne < letterTwo and letterOne > letterThree:
    print(f"The letter in the middle is {letterOne}")
elif letterTwo > letterOne and letterTwo < letterThree or letterTwo < letterOne and letterTwo > letterThree:
    print(f"The letter in the middle is {letterTwo}")
else:
    print(f"The letter in the middle is {letterThree}")