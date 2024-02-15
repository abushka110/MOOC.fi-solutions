# solution
# function check if blocks are correct in sudoku
def sudoku_block_correct(sudoku: list):
    for row_no in range(0, 7, 3):
        for column_no in range(0, 7, 3):
            numbers = []
            for row in range(row_no, row_no + 3):
                for column in range(column_no, column_no + 3):
                    number = sudoku[row][column]
                    if number > 0 and number in numbers:
                        return False
                    numbers.append(number)
    return True

# function check if rows are correct in sudoku
def sudoku_row_correct(sudoku: list):
    for row_no in range(0, 7):
        numbers = []
        for element in sudoku[row_no]:
            if element > 0 and element in numbers:
                return False
            numbers.append(element)
    return True

# function check if columns are correct in sudoku
def sudoku_column_correct(sudoku: list):
    for column_no in range(0, 7):
        numbers = []
        for row_no in range(0, 7):
            number = sudoku[row_no][column_no]
            if number > 0 and number in numbers:
                return False
            numbers.append(number)
    return True

# function check if grid is correct in sudoku
def sudoku_grid_correct(sudoku: list):
    if sudoku_block_correct(sudoku) == False:
        return False
    
    if sudoku_row_correct(sudoku) == False:
        return False
    
    if sudoku_column_correct(sudoku) == False:
        return False
    
    return True

# test
sudoku1 = [
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

print(sudoku_grid_correct(sudoku1)) # False

sudoku2 = [
  [2, 6, 7, 8, 3, 9, 5, 0, 4],
  [9, 0, 3, 5, 1, 0, 6, 0, 0],
  [0, 5, 1, 6, 0, 0, 8, 3, 9],
  [5, 1, 9, 0, 4, 6, 3, 2, 8],
  [8, 0, 2, 1, 0, 5, 7, 0, 6],
  [6, 7, 4, 3, 2, 0, 0, 0, 5],
  [0, 0, 0, 4, 5, 7, 2, 6, 3],
  [3, 2, 0, 0, 8, 0, 0, 5, 7],
  [7, 4, 5, 0, 0, 3, 9, 0, 1]
]

print(sudoku_grid_correct(sudoku2)) # True

sudoku3 = [
  [ 6, 4, 9, 2, 8, 3, 1, 5, 7 ],
  [ 0, 5, 0, 6, 4, 9, 2, 3, 8 ],
  [ 2, 3, 8, 1, 5, 7, 6, 4, 9 ],
  [ 9, 2, 3, 8, 1, 5, 0, 6, 4 ],
  [ 7, 6, 4, 9, 2, 3, 8, 1, 5 ],
  [ 8, 1, 5, 7, 0, 4, 9, 2, 0 ],
  [ 5, 7, 6, 4, 9, 2, 3, 2, 1 ],
  [ 4, 0, 2, 3, 8, 1, 5, 0, 6 ],
  [ 3, 0, 1, 5, 0, 6, 4, 9, 0 ],
]

print(sudoku_grid_correct(sudoku3)) # False