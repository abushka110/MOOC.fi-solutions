# solution
def distinct_numbers(numbersList: list):
    distinctList = []
    for number in numbersList:
        if number not in distinctList:
            distinctList.append(number)
    return sorted(distinctList)


# test
my_list = [3, 2, 2, 1, 3, 3, 1]
print(distinct_numbers(my_list)) # [1, 2, 3]