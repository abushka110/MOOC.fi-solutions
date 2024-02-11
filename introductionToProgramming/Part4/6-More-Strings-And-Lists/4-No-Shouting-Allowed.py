# solution
def no_shouting(wordsList: list):
    wordsNoUpper = []
    for word in wordsList:
        if not word.isupper():
            wordsNoUpper.append(word)
    return wordsNoUpper

# test
if __name__ == "__main__":
    my_list = ["ABC", "def", "UPPER", "ANOTHERUPPER", "lower", "another lower", "Capitalized"]
    pruned_list = no_shouting(my_list)
    print(pruned_list) # ['def', 'lower', 'another lower', 'Capitalized']