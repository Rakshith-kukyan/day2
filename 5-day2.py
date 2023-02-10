def print_row_col_sums(matrix):
    num_rows = len(matrix)
    num_cols = len(matrix[0])

    row_sums = []
    for i in range(num_rows):
        row_sum = 0
        for j in range(num_cols):
            row_sum += matrix[i][j]
        row_sums.append(row_sum)
    print("Row sums:", row_sums)

    col_sums = []
    for j in range(num_cols):
        col_sum = 0
        for i in range(num_rows):
            col_sum += matrix[i][j]
        col_sums.append(col_sum)
    print("Column sums:", col_sums)

matrix = [
    [1, 2, 3,4],
    [ 5, 6,7,8],
    [9,10,11,12]
]
print("Row and column sums of the matrix:")
print_row_col_sums(matrix)