# solution model
def row_sums(my_matrix: list):
    for matrix_row in my_matrix:
        matrix_row.append(sum(matrix_row))
        
# solution
def row_sums(my_matrix: list):
    for matrix_row in my_matrix:
        sum = 0
        for row_element in matrix_row:
            sum += row_element
        matrix_row.append(sum)

# test
if __name__ == "__main__":
    my_matrix = [[1, 2], [3, 4]]
    row_sums(my_matrix)
    print(my_matrix)
    # Sample output
    # [[1, 2, 3], [3, 4, 7]]
