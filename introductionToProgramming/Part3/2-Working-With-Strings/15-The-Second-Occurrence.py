word = input("Please type in a string: ")
character = input("Please type in a substring: ")

indexChar = word.find(character)

if indexChar == -1:
    print("The substring does not occur twice in the string.")
else:
    indexChar = word.find(character, indexChar + len(character))
    if indexChar == -1:
        print("The substring does not occur twice in the string.")
    else:
        print(f"The second occurrence of the substring is at index {indexChar}.")