word = input("Word: ")

charNum = 30
charNumMin2 = charNum - 2
halfLen = int((charNumMin2 - len(word)) / 2)

print("*" * charNum)
if len(word) % 2 == 0:
    print("*" + " " * halfLen + f"{word}" + " " * halfLen + "*")
else:
    print("*" + " " * halfLen + f"{word}" + " " * (halfLen + 1) + "*")
print("*" * charNum)