def range_of_list(numbersList):
    return max(numbersList) - min(numbersList)

# You can test your function by calling it within the following block
if __name__ == "__main__":
    # test 1
    my_list = [3, 6, -4]
    result = range_of_list(my_list)
    print(result)
    # test 2
    my_list = [1, 2, 3, 4, 5]
    result = range_of_list(my_list)
    print("The range of the list is", result)