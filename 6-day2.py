def print_center_column(matrix):
    num_rows = len(matrix)
    num_cols = len(matrix[0])

    if num_cols % 2 == 0:
        center_col = num_cols // 2 
    else:
        center_col = num_cols // 2 

    for i in range(num_rows):
        result.append(matrix[i][center_col])
    print(result)

matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]
result=[]
print("Center column of the matrix:")
print_center_column(matrix) 