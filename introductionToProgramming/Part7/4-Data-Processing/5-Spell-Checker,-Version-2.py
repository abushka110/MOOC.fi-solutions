# solution
from difflib import get_close_matches

sentence = input("write text: ")
sentence_list = sentence.split(" ")
sentence_checked = ""

# add words from txt file
wordlist = []
with open("wordlist.txt") as wordlist_file:
    for word in wordlist_file:
        word = word.replace("\n", "")
        wordlist.append(word)

wrong_words = []
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
        wrong_words.append(sentence_word)
        sentence_checked += f"*{sentence_word}* "

# print checked sentence
print(sentence_checked)
print("suggestions:")

for wrong_word in wrong_words:
    close_matches = get_close_matches(wrong_word, wordlist)
    sentence_suggestions = f"{wrong_word}: "
    for word in close_matches:
        sentence_suggestions += f"{word}, "
    print(sentence_suggestions[:-2])

# test
if __name__ == "__main__":
    pass  # Add your test code here
