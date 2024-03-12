# solution
from string import ascii_lowercase, ascii_uppercase, punctuation
def separate_characters(my_string: str):
    string_ascii = ''
    string_punctuation = ''
    string_other = ''
    for char in my_string:
        if char in ascii_lowercase or char in ascii_uppercase:
            string_ascii += char
        elif char in punctuation:
            string_punctuation += char
        else:
            string_other += char
    return (string_ascii, string_punctuation, string_other)


# test
if __name__ == "__main__":
    parts = separate_characters("Olé!!! Hey, are ümläüts wörking?")
    print(parts[0])
    print(parts[1])
    print(parts[2])
    # should print out:
    # OlHeyaremltswrking
    # !!!,?
    # é  üäü ö