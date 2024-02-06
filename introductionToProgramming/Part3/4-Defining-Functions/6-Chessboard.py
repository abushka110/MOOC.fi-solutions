# solution 1, correct only for odd numbers
# def chessboard(columns):
#     rows = columns
#     binary = ""
#     index = 1
#     while rows <= columns * columns:
#         while index <= rows:
#             if index % 2 == 0:
#                 binary += "0"
#             else:
#                 binary += "1"
#             index += 1
#         print(binary)
#         binary = ""
#         rows += columns
    

# Testing the function
if __name__ == "__main__":
    chessboard(8)
    print(" ")
    chessboard(7)