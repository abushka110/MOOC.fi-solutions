# solution
from random import choice

def words(n: int, beginning: str):
    words = []
    with open("words.txt") as words_file:
        for line in words_file:
            line.replace("\n", "")
            words.append(line)

    compatible_words = []
    for word in words:
        if word[:len(beginning)] == beginning:
            compatible_words.append(word)
    
    word_list = []
    if n <= len(compatible_words):
        for i in range(n):
            word_to_add = choice(compatible_words)
            while word_to_add in word_list:
                word_to_add = choice(compatible_words)
            word_list.append(word_to_add)
    else:
        raise ValueError

    return word_list

# test
if __name__ == "__main__":
    word_list = words(3, "ca")
    for word in word_list:
        print(word)
    # output will be like:
    # cat
    # car
    # carbon