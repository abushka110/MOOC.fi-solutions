#  solution 
def all_the_longest(wordsList: list):
    longestList = [""]
    for word in wordsList:
        if len(longestList[0]) < len(word):
            longestList[0] = word
    for word in wordsList:
        if len(longestList[0]) == len(word) and longestList[0] != word:
            longestList.append(word)
    return longestList

# test 1
my_list = ["first", "second", "fourth", "eleventh"]
result = all_the_longest(my_list)
print(result) # ['eleventh']

# test 2
my_list = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]
result = all_the_longest(my_list)
print(result) # ['dorothy', 'richard']