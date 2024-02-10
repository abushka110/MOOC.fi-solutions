# solution
def everything_reversed(wordsList: list):
    reversedWordsList = []
    for word in wordsList:
        reversedWordsList.append(word[::-1])
    return reversedWordsList[::-1]

# test
if __name__ == "__main__":
    # test 1
    my_list = ["Hi", "there", "example", "one more"]
    new_list = everything_reversed(my_list)
    print(new_list) # ['erom eno', 'elpmaxe', 'ereht', 'iH']

    # test 2
    new_list = everything_reversed(['abc'])
    print(new_list) # ['cba']