# solution
import random

def word_generator(characters: str, length: int, amount: int):
    return(''.join(random.sample(characters, length)) for i in range(amount))

# test
if __name__ == "__main__":
    word_gen = word_generator("abcdefg", 3, 5)
    for word in word_gen:
        print(word)
    # expected output:
    # dbf
    # baf
    # ead
    # fga
    # ccc