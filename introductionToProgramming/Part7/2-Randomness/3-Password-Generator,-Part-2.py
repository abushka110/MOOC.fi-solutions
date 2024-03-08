# solution
# solution 1
from random import choice
from string import ascii_lowercase
 
def generate_strong_password(length: int, add_num: bool, add_special_char: bool):
    passwd = ""
    while len(passwd) < length:
        passwd += choice(ascii_lowercase)
 
    return passwd

# test
if __name__ == "__main__":
    for i in range(10):
    print(generate_strong_password(8, True, True))