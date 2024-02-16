# solution
def double_items(numbers_list: list):
    new_list = []
    for number in numbers_list:
        new_list.append(number * 2)
    return new_list

# test
if __name__ == "__main__":
    numbers = [2, 4, 5, 3, 11, -4]
    numbers_doubled = double_items(numbers)
    print("original:", numbers)
    print("doubled:", numbers_doubled)