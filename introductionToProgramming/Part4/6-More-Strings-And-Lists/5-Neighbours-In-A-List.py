# # my solution
# def longest_series_of_neighbours(numbersList: list):
#     neighboursCount = 0
#     tempCount = 0
#     for x in range(0, len(numbersList)):
#         if x < len(numbersList) - 1:
#             if numbersList[x] + 1 == numbersList[x + 1] or numbersList[x] - 1 == numbersList[x + 1] or numbersList[x] == numbersList[x + 1] :
#                 tempCount += 1
#             else:
#                 tempCount = 0
#         if neighboursCount < tempCount:
#             neighboursCount = tempCount
#     return neighboursCount + 1

# model solution
def longest_series_of_neighbours(my_list: list):
    longest = 1
    result = 1
    for i in range(1, len(my_list)):
        # function abs calculates the absolute value
        if abs(my_list[i-1]-my_list[i]) == 1:
            result += 1
        else:
            result = 1
        # function max returns the highest of the parameters
        longest = max(longest, result)
    return longest


# test
if __name__ == "__main__":
    my_list = [1, 2, 5, 7, 6, 5, 6, 3, 4, 1, 0]
    print(longest_series_of_neighbours(my_list))