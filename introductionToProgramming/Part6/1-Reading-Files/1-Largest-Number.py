# solution
def largest():
    largest_num = 0
    with open("numbers.txt") as nums_file:
        for num in nums_file:
            if int(num) > largest_num:
                largest_num = int(num)
    return largest_num

print(largest())