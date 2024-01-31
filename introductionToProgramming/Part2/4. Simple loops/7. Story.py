wordCurrent = input("Please type in a word: ")
wordPrevious = " "
story = ""

while True:
    if wordCurrent != "end" and wordCurrent != wordPrevious:
        story += f" {wordCurrent}"
        wordPrevious = wordCurrent
        wordCurrent = input("Please type in a word: ")
    else:
        break

print(story)