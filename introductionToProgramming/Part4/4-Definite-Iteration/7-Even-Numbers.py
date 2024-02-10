def even_numbers(numbersList: list):
    evenList = []
    for item in numbersList:
        if item % 2 == 0:
            evenList.append(item)
    return evenList

# test
my_list = [1, 2, 3, 4, 5]
new_list = even_numbers(my_list)
print("original", my_list)
print("new", new_list)