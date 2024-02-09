# solution
def sum_of_positives(listOfNumbers: list):
    sum = 0
    for item in listOfNumbers:
        if item > 0:
            sum += item
    return sum

# test
my_list = [1, -2, 3, -4, 5]
result = sum_of_positives(my_list)
print("The result is", result)