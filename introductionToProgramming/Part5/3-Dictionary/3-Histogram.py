# solution
def histogram(word: str):
    chars = {}
    for char in range(len(word)):
        if word[char] not in chars:
            chars[word[char]] = 0
        chars[word[char]] += 1
    for key, value in chars.items():
        print(key, "*" * value)

# test
if __name__ == "__main__":
    histogram("abba")
    print()
    histogram("statistically")