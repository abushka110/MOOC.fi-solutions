# solution
sentence = input("Write text: ")
sentence_list = sentence.split(" ")
sentence_checked = ""

wordlist = []
with open("wordlist.txt") as wordlist_file:
    for word in wordlist_file:
        word = word.replace("\n", "")
        wordlist.append(word)


for sentence_word in sentence_list:
    index = 0
    for word in wordlist:
        if word.upper() == sentence_word.upper():
            index = 1
    if index == 1:
        sentence_checked += f"{sentence_word} "
    else:
        sentence_checked += f"*{sentence_word}* "
    
print(sentence_checked)