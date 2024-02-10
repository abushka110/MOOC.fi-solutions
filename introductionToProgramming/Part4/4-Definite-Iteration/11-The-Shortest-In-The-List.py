# solution
def shortest(wordsList: list):
    shortestWord = wordsList[0]
    for item in wordsList:
        if len(shortestWord) > len(item):
            shortestWord = item
    return shortestWord


# test 1
my_list = ["first", "second", "fourth", "eleventh"]
result = shortest(my_list)
print(result) # first

# test 2
my_list = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]
result = shortest(my_list)
print(result) # tim