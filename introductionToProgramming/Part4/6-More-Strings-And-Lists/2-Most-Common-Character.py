# # solution
# def most_common_character(word: str):
#     wordList = []
#     for index in range(0, len(word)):
#         wordList.append(word[index])
#     charList = []
#     charCountList = []
#     for item in wordList:
#         if item not in charList:
#             charList.append(item)
#             charCountList.append(wordList.count(item))
#     return charList[charCountList.index(max(charCountList))]

# better solution
def most_common_character(word: str):
    mcChar = word[0]
    for character in word:
        if word.count(character) > word.count(mcChar):
            mcChar = character
    return mcChar



# test
if __name__ == "__main__":
    first_string = "abcdbde"
    print(most_common_character(first_string)) # b

    second_string = "exemplaryelementary"
    print(most_common_character(second_string)) # e