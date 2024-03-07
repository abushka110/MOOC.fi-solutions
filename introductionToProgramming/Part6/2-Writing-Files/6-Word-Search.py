# solution
def find_words(word: str):
    # add words from file to list
    words_list = []
    with open("words.txt") as words_file:
        for line in words_file:
            line = line.replace("\n", "")
            words_list.append(line)

    found_words_list = []
    for word_search in words_list:
        # check if ord has a dot
        if "." in word and len(word) == len(word_search):
            index = 0
            for char_word, char_search in zip(word, word_search):
                if char_word != '.' and char_word != char_search:
                    index += 1
            if index == 0:
                found_words_list.append(word_search)
        # "*" at the beginning means that any word which ends with the search term is acceptable
        elif word[0] == "*" and word_search.endswith(word[1:]):
            found_words_list.append(word_search)
        # "*" at the end of the search term means that any word which begins with the search term is acceptable
        elif word[-1] == "*" and word_search.startswith(word[:-1]):
            found_words_list.append(word_search)
        # if there are no special characters, only words that match the search term exactly are returned
        elif word == word_search:
            found_words_list.append(word_search)
    
    # return found words
    return found_words_list


# test
if __name__ == "__main__":
    # test 1
    print(find_words("*vokes"))
    # ['convokes', 'equivokes', 'evokes', 'invokes', 'provokes', 'reinvokes', 'revokes']

    # test 2
    print(find_words("abu*"))
    # ['abubble', 'abundance', 'abundances', 'abundant', 'abundantly', 'abusable', 'abusage', 'abuse', 'abused', 'abuser', 'abusers', 'abuses', 'abusing', 'abusive', 'abusively', 'abusiveness', 'abut', 'abutment', 'abutments', 'abuts', 'abuttal', 'abuttals', 'abutted', 'abutter', 'abutters', 'abutting', 'abuzz']

    # test 3
    print(find_words("ca."))
    # ['cab', 'cad', 'cal', 'cam', 'can', 'cap', 'car', 'cat', 'caw', 'cay']

    # test 4
    print(find_words("p.ng"))
    # ['pang', 'ping', 'pong']

    # test 5
    print(find_words(".a.e"))
    # ['sane', 'care', 'late']