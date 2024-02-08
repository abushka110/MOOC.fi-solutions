words = []

word = input("Word: ")

while word not in words:
    words.append(word)
    word = input("Word: ")
    
print(f"You typed in {len(words)} different words")