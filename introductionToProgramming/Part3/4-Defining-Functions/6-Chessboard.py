# solution 1, while loop
def chessboard(columns):
    index1 = 0
    index2 = 0
    binary = ""
    while index1 < columns:
        while index2 < columns:
            if (index1 + index2) % 2 == 0:
                binary += "1"
            else:
                binary += "0"
            index2 +=  1
        print(binary)
        binary = ""
        index1 += 1
        index2 = 0

# # solution 2, for loop
# def chessboard(columns):
#     binary = ""
#     for x in range(0, columns):
#         for j in range(0, columns):
#             if (x + j) % 2 == 0:
#                 binary += "1"
#             else:
#                 binary += "0"
#         print(binary)
#         binary = ""

# # model solution
# def chessboard(size):
#     i = 0
#     while i < size:
#         if i % 2 == 0:
#             row = "10"*size
#         else:
#             row = "01"*size
#         # Remove extra characters at the end of the row
#         print(row[0:size])
#         i += 1

# Testing the function
if __name__ == "__main__":
    chessboard(4)
    print(" ")
    chessboard(3)
