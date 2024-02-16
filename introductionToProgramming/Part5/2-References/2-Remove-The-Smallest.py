# solution
def remove_smallest(numbers_list: list):
    smallest_number = min(numbers_list)
    numbers_list.remove(smallest_number)

# test
if __name__ == "__main__":
    numbers = [2, 4, 6, 1, 3, 5]
    remove_smallest(numbers)
    print(numbers)