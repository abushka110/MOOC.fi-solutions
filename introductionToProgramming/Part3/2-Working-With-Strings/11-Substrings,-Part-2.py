word = input("Please type in a string: ")

numWord = len(word) - 1

while numWord >= 0:
    print(word[numWord:])
    numWord -= 1