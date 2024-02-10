# solution
def no_vowels(someString: str):
    stringWithoutVowels = ""
    vowels = ["a", "e", "i", "o", "u"]
    for char in someString:
        if char not in vowels:
            stringWithoutVowels += char
    return stringWithoutVowels

# test
if __name__ == "__main__":
    my_string = "this is an example"
    print(no_vowels(my_string)) # ths s n xmpl

    print(no_vowels("aeoli")) # l