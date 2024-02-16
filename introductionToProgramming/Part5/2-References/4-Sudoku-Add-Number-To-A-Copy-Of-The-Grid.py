# solution
# function that print out sudoku
def print_sudoku(sudoku_grid: list):
    for row_no in range(0, len(sudoku_grid)):
        for column_no in range(0, len(sudoku_grid)):
            character = sudoku_grid[row_no][column_no]
            if sudoku_grid[row_no][column_no] == 0:
                character = "_"
            if (column_no + 1) % 3 == 0:
                print(f"{character}  ", end="")
            else:
                print(f"{character} ", end="")
        print()
        if (row_no + 1) % 3 == 0:
            print()

# function that add number to sudoku
def copy_and_add(sudoku_grid: list, row_no: int, column_no: int, value: int):
    sudoku_grid_copy = []
    for row in sudoku_grid:
        sudoku_grid_copy.append(row[:])
    sudoku_grid_copy[row_no][column_no] = value
    return sudoku_grid_copy

# test
if __name__ == "__main__":
    sudoku  = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]

    grid_copy = copy_and_add(sudoku, 0, 0, 2)
    print("Original:")
    print_sudoku(sudoku)
    print()
    print("Copy:")
    print_sudoku(grid_copy)