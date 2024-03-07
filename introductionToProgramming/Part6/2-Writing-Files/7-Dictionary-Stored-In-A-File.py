# solution
# ask for first action
print("1 - Add word, 2 - Search, 3 - Quit")
function = int(input("Function: "))

# add existing words translation to dict
words_dict = {}
with open("dictionary.txt") as words_file_read:
    for line in words_file_read:
        line = line.replace("\n", "")
        line = line.split(";")
        words_dict[line[0]] = line[1]

# don't quit until function is not 3
while function != 3:
    # add translation
    if function == 1:
        # ask for translation
        translate_finnish = input("The word in Finnish: ")
        translate_english = input("The word in English: ")
        # add translation to dict
        words_dict[translate_finnish] = translate_english
        # add translation to file
        with open("dictionary.txt", "a") as words_file_write:
            words_file_write.write(f"{translate_finnish};{translate_english}\n")
        print("Dictionary entry added")
    # search for translation
    elif function == 2:
        word_find = input("Search term: ")
        for finnish, english in words_dict.items():
            if word_find in english or word_find in finnish:
                print(f"{finnish} - {english}")

    print("1 - Add word, 2 - Search, 3 - Quit")
    function = int(input("Function: "))
# print when user quit
print("Bye!")


# # solution 1
# # add existing words translation to dict
# words_dict = {}
# with open("dictionary.txt") as words_file_read:
#     for line in words_file_read:
#         line = line.replace("\n", "")
#         line = line.split(";")
#         words_dict[line[0]] = line[1]

# def add_translation(words: dict):
#     # ask for translation
#     translate_finnish = input("The word in Finnish: ")
#     translate_english = input("The word in English: ")
#     # add translation to dict
#     words[translate_finnish] = translate_english
#     # add translation to file
#     with open("dictionary.txt", "a") as words_file_write:
#         words_file_write.write(f"{translate_finnish};{translate_english}\n")

# def find_translation(words: dict):
#     word_find = input("Search term: ")
#     for finnish, english in words.items():
#         if word_find in english or word_find in finnish:
#             print(f"{finnish} - {english}")

# # ask for first action
# print("1 - Add word, 2 - Search, 3 - Quit")
# function = int(input("Function: "))

# # don't quit until function is not 3
# while function != 3:
#     # add translation
#     if function == 1:
#         add_translation(words_dict)
#         print("Dictionary entry added")
#     # search for translation
#     elif function == 2:
#         find_translation(words_dict)
#     print("1 - Add word, 2 - Search, 3 - Quit")
#     function = int(input("Function: "))

# # print when user quit
# print("Bye!")