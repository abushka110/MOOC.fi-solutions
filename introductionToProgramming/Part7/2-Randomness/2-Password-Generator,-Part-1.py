# solution
# from random import shuffle
# def generate_password(length: int):
#     password = ""
#     letters = 'abcdefghijklmnopqrstuvwxyz'
#     letters_list = []
#     for letter in letters:
#         letters_list.append(letter)
#     shuffle(letters_list)
#     index = 0
#     while len(password) < length:
#         password += letters_list[index]
#         index += 1
#     return password

# solution 1
from random import choice
from string import ascii_lowercase
 
def generate_password(length: int):
    passwd = ""
    while len(passwd) < length:
        passwd += choice(ascii_lowercase)
 
    return passwd

# test
if __name__ == "__main__":
    for i in range(10):
        print(generate_password(8))
