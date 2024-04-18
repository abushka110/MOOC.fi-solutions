# solution
sentence = input("Write text: ")
sentence_list = sentence.split(" ")
sentence_checked = ""

# add words from txt file
wordlist = []
with open("wordlist.txt") as wordlist_file:
    for word in wordlist_file:
        word = word.replace("\n", "")
        wordlist.append(word)

# check if spelling - right
for sentence_word in sentence_list:
    index = 0
    for word in wordlist:
        # if word found in the word list from txt file
        if word.upper() == sentence_word.upper():
            index = 1
    # if word found, it won't be marked
    if index == 1:
        sentence_checked += f"{sentence_word} "
    # if word not found (spelled wrong) - word will be marked with ""
    else:
        sentence_checked += f"*{sentence_word}* "

# print checked sentence
print(sentence_checked)