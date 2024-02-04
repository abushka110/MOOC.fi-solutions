# solution 1
# num  = int(input("Please type in a number: "))

# index = 0

# if num % 2 == 0:
#     while index < num:
#         index+= 2
#         print(index)
#         index -= 1
#         print(index)
#         index += 1
# else:
#     while index < num - 1:
#         index += 2
#         print(index)
#         index -= 1
#         print(index)
#         index += 1
#     print(num)

# solution 2
# num  = int(input("Please type in a number: "))

# index = 0

# if num % 2 == 0:
#     while index < num:
#         index+= 2
#         print(index)
#         print(index - 1)
# else:
#     while index < num - 1:
#         index+= 2
#         print(index)
#         print(index - 1)
#     print(num)

# solution 3
num  = int(input("Please type in a number: "))

index = 1

while index + 1 <= num:
    print(index + 1)
    print(index)
    index += 2

if index <= num:
    print(index)