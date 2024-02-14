# solution
def column_correct(sudoku: list, column_no: int):
    sudoku_column = []
    for row in sudoku:
        sudoku_column.append(row[column_no])
            
    check_list = list(range(1, 10))
    for number in check_list:
        if sudoku_column.count(number) > 1:
            return False

    return True

# model solution
# def column_correct(sudoku: list, column_no: int):
#     numbers = []
#     for row in sudoku:
#         number = row[column_no]
#         if number > 0 and number in numbers:
#             return False
#         numbers.append(number)
#     return True

# test
sudoku = [
  [9, 0, 0, 0, 8, 0, 3, 0, 0],
  [2, 0, 0, 2, 5, 0, 7, 0, 0],
  [0, 2, 0, 3, 0, 0, 0, 0, 4],
  [2, 9, 4, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 7, 3, 0, 5, 6, 0],
  [7, 0, 5, 0, 6, 0, 4, 0, 0],
  [0, 0, 7, 8, 0, 3, 9, 0, 0],
  [0, 0, 1, 0, 0, 0, 0, 0, 3],
  [3, 0, 0, 0, 0, 0, 0, 0, 2]
]

print(column_correct(sudoku, 0)) # False
print(column_correct(sudoku, 1)) # True