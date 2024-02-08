def mean(numbersList: list):
    return sum(numbersList) / len(numbersList)

# solution withou sum and len functions
# def mean(numbersList: list):
#     index = 0
#     sum = 0
#     while index < len(numbersList):
#         sum += numbersList[index]
#         index += 1
#     mean = sum / index
#     return mean

# You can test your function by calling it within the following block
if __name__ == "__main__":
    # test 1
    my_list = [1, 2, 3, 4, 5]
    result = mean(my_list)
    print("mean value is", result)
    # test 2
    my_list = [3, 6, -4]
    result = mean(my_list)
    print(result)
