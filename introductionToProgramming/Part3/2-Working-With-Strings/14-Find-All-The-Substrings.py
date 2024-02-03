word = input("Please type in a word: ")
character = input("Please type in a character: ")

indexChar = word.find(character)

while indexChar != -1 and len(word) >= indexChar + 3:
    print(word[indexChar:indexChar+3])
    word = word[indexChar + 1:]
    indexChar = word.find(character)
