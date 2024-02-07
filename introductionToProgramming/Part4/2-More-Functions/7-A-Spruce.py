# solution 1
# Write your solution here
# def spruce(size):
#     print("a spruce!")
#     index = 0
#     size1= size - 1
#     outputEnd = ""
#     while index < size:
#         if index == 0:
#             output = (" " * size1) + ("*")
#             print(output)
#             outputEnd = output
#         else:
#             output = (" " * size1) + ("*" * (index * 2) + "*")
#             print(output)
#         size1 -= 1
#         index += 1
#     print(outputEnd)

# solution 2
def spruce(size):
    print("a spruce!")
    i = 1
    while i <= size:
        emptySpace = size - i
        stars = 2 * i -1
        print(" " * emptySpace + "*" * stars)
        i += 1
    print(" " * (size - 1) + "*")

# You can test your function by calling it within the following block
if __name__ == "__main__":
    spruce(3)