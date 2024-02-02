word = input("Word: ")

charNum = 30

spacesAtStart = (charNum - 2 - len(word)) // 2
spacesAtEnd = spacesAtStart

print("*" * charNum)
if len(word) % 2 != 0:
    spacesAtEnd += 1

print("*" + " " * spacesAtStart + f"{word}" + " " * spacesAtEnd + "*")
print("*" * charNum)