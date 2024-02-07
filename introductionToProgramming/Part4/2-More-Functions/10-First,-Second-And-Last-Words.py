# solution 1
# # Write your solution here
# def first_word(sentence):
#     index = 0
#     while sentence[index] != " ":
#         index += 1
#     return sentence[:index]

# def second_word(sentence):
#         index = 0
#         while sentence[index] != " ":
#             index += 1
#         index2 = index + 1
#         while sentence[index2] != " ":
#             index2 += 1
#             if index2 == len(sentence):
#                 break
#         return sentence[index + 1: index2]

# def last_word(sentence):
#     index = len(sentence) - 1
#     while sentence[index] != " ":
#         index -= 1
#     return sentence[index + 1:]

# modle solution
def find_word(str, whatth):
    index = 0
    word = ""
    counter = 0
    while index < len(str):
        if str[index] == " ":
            counter += 1
            if counter == whatth:
                break
            word = ""
        else:
            word += str[index]
        index += 1
    return word
 
def first_word(mjono):
    return find_word(mjono, 1)
 
def second_word(mjono):
    return find_word(mjono, 2)
 
def last_word(mjono):
    return find_word(mjono, 0)


# You can test your function by calling it within the following block
if __name__ == "__main__":
    sentence = "first second"
    print(first_word(sentence))
    print(second_word(sentence))
    print(last_word(sentence))