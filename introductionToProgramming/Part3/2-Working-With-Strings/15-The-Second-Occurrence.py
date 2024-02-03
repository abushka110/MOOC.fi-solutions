word = input("Please type in a string: ")
character = input("Please type in a substring: ")

lenOfChar = len(character)

indexChar = word.find(character)

secondWordIndex = 0

index2 = 0

while indexChar != -1 or index2 != 2:
    secondWordIndex += indexChar
    index2 += 1
    if lenOfChar == 2:
        word = word[indexChar+2:]
        secondWordIndex += 1
    else:
        word = word[indexChar+1:]
    indexChar = word.find(character)

if index2 == 2:
    print(f"The second occurrence of the substring is at index {secondWordIndex}.")
else:
    print("The substring does not occur twice in the string.")
