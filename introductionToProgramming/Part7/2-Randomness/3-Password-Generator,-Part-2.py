# solution
from random import choice, randint, random
from string import ascii_lowercase, digits

def generate_strong_password(pass_length, bool_num, bool_special_char):
    passwd = choice(ascii_lowercase)  # Add a lowercase letter to the password
    special_chars = "!?=+-()#"
    while len(passwd) < pass_length:
        if bool_num and bool_special_char:
            if random() < 0.5:  # Randomly choose between number and special character
                passwd += str(randint(0, 9))
            else:
                passwd += choice(special_chars)
        elif bool_num:
            passwd += str(randint(0, 9))
        elif bool_special_char:
            passwd += str(choice(special_chars))
        else:
            passwd += choice(ascii_lowercase)

    if not any(char.isascii() for char in passwd):
        passwd.replace(passwd[randint(0, len(passwd) - 1)], choice(ascii_lowercase))
 
    return passwd

# test 
# if __name__ == "__main__":
#     for i in range(10):
#         print(generate_strong_password(8, True, True))