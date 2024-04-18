# solution
from difflib import get_close_matches

sentence = input("write text: ")

# add words from txt file
wordList = []
with open("wordlist.txt") as wordList_file:
    for word in wordList_file:
        word = word.replace("\n", "")
        wordList.append(word)

wrong_words = []
# check if spelling wright
for sentence_word in sentence.split(" "):
    if sentence_word.lower() in wordList:
        print(f"{sentence_word} ", end="")
    else:
        wrong_words.append(sentence_word)
        print(f"*{sentence_word}* ", end="")

print()

# print suggestions
print("suggestions:")
for wrong_word in wrong_words:
    suggestion_list = get_close_matches(wrong_word, wordList)
    suggestions = ", ".join(suggestion_list)
    print(f"{wrong_word}: {suggestions}")
