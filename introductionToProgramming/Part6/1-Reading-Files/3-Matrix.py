# solution
def matrix_build():
    with open("matrix.txt") as matrix_elements_file:
        matrix = []
        for line in matrix_elements_file:
            m_row = []
            items = line.split(",")
            for item in items:
                m_row.append(int(item))
            matrix.append(m_row)
    return matrix

def combine(matrix: list):
    matrix_list = []
    for row in matrix:
        matrix_list += row
    return matrix_list

def matrix_sum():
    m_list = combine(matrix_build())
    return sum(m_list)

def matrix_max():
    m_list = combine(matrix_build())
    return max(m_list)

def row_sums():
    matrix = matrix_build()
    sums = []
    for row in matrix:
        sums.append(sum(row))
    return sums

matrix_sum()
matrix_max()
row_sums()