# solution
# def transpose(matrix: list):
#     new_list = []
#     for row in matrix:
#         new_list.append(row[:])
#     for row_no in range(0, len(matrix)):
#         for column_no in range(0, len(matrix)):
#             new_list[column_no][row_no] = matrix[row_no][column_no]
#     for row in range(0, len(new_list)):
#         for column in range(0, len(new_list)):
#             matrix[row][column] = new_list[row][column]

# model solution
def transpose(matrix: list):
    for i in range(0, len(matrix)):
        for j in range(i, len(matrix)):
            temp = matrix[i][j]
            matrix[i][j] = matrix[j][i]
            matrix[j][i] = temp


# test
if __name__ == "__main__":
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    transpose(matrix)
    print(matrix)