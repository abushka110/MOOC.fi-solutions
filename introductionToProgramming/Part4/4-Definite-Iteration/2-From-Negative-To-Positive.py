number = int(input("Please type in a positive integer: "))

for i in range(-number, number + 1):
    # solution 1
    # if i != 0:

    # model solution
    #     print(i)
    # Because in Python bool-type equals to
    # 0 and 1 (False and True), condition can also be written as follows
    if i:
        print(i)