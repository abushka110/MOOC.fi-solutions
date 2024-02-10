# solution
def list_sum(list: list, list1: list):
    sumList = []
    for index in range (0, len(list1)):
        sumList.append(list[index] + list1[index])
    # solution 2
    # for item1, item2 in zip(list1, list2):
    #     results.append(item1 + item2)
    return sumList

# test
a = [1, 2, 3]
b = [7, 8, 9]
print(list_sum(a, b)) # [8, 10, 12]