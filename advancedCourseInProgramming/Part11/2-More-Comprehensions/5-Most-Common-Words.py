# solution
from string import punctuation

def most_common_words(filename: str, lower_limit: int):
    text = ""
    with open(filename) as file:
        text = file.read()
        # remove punctuation marks from strings
        for punctuation_mark in punctuation:
            text = text.replace(punctuation_mark, "")
    
    # split text into strings in list
    text_strings = text.split()

    return {word : text_strings.count(word) for word in text_strings if text_strings.count(word) >= lower_limit}

# test
if __name__ == "__main__":
    print(most_common_words("src/comprehensions.txt", 3))