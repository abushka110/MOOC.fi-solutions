# solution
def length_of_longest(wordsList: list):
    longestWordLen = 0
    for item in wordsList:
        if len(item) > longestWordLen:
            longestWordLen = len(item)
    return longestWordLen

# test 1
my_list = ["first", "second", "fourth", "eleventh"]
result = length_of_longest(my_list)
print(result) # 8

# test 2
my_list = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]
result = length_of_longest(my_list)
print(result) # 7