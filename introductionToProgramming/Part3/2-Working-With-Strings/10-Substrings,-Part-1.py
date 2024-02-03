word = input("Please type in a string: ")

numWord = 1

while numWord <= len(word):
    print(word[0:numWord])
    numWord += 1