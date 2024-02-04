word = input("Please type in a sentence: ")

index = 0

while index != -1:
    print(word[0])
    index = word.find(" ")
    word = word[index + 1:]
