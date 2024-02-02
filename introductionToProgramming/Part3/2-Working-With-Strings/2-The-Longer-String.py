wordOne = input("Please type in string 1: ")
wordTwo = input("Please type in string 2: ")

if len(wordOne) < len(wordTwo):
    print(f"{wordTwo} is longer")
elif len(wordOne) > len(wordTwo):
    print(f"{wordOne} is longer")
else:
    print("The strings are equally long")
