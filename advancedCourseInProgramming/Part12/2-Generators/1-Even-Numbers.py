# solution
def even_numbers(beginning: int, maximum: int):
    if beginning % 2 != 0:
        beginning += 1
    while beginning <= maximum:
        yield beginning
        beginning += 2

# test
if __name__ == "__main__":
    # test 1
    numbers = even_numbers(2, 10)
    for number in numbers:
        print(number)
    # expected output:
    # 2
    # 4
    # 6
    # 8
    # 10

    print()

    # test 2
    numbers = even_numbers(11, 21)
    for number in numbers:
        print(number)
    # expected output:
    # 12
    # 14
    # 16
    # 18
    # 20