# solution
def longest(words: list):
    # function returns longest item in list
    longestWord = words[0]
    for word in words:
        if len(word) > len(longestWord):
            longestWord = word
    return longestWord

# test
if __name__ == "__main__":
    strings = ["hi", "hiya", "hello", "howdydoody", "hi there"]
    print(longest(strings)) # howdydoody