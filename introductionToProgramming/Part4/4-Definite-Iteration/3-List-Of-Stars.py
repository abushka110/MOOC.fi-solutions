# solution 1
def list_of_stars(numbers: list):
    for number in numbers:
        print("*" * number)

# solution 2
# def list_of_stars(numbers: list):
#     for i in range (0, len(numbers)):
#         print("*" * numbers[i])

# function test
list_of_stars([3, 7, 1, 1, 2])