# solution
def count_matching_elements(my_matrix: list, element: int):
    matchCount = 0
    for item in my_matrix:
        for number in item:
            if number == element:
                matchCount += 1
    return matchCount

# test
m = [[1, 2, 1], [0, 3, 4], [1, 0, 0]]
print(count_matching_elements(m, 1)) # 3