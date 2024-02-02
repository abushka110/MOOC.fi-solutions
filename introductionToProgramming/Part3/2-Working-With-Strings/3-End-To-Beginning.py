word = input("Please type in a string: ")

wordLength = len(word)

while wordLength != 0:
    print(word[wordLength - 1])
    wordLength -= 1