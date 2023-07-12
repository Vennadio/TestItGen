def minimum(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    min_row_sum = float('inf')
    min_row_index = -1

    # Находим строку с минимальной суммой
    for i in range(rows):
        row_sum = sum(matrix[i])
        if row_sum < min_row_sum:
            min_row_sum = row_sum
            min_row_index = i

    min_col_sum = float('inf')
    min_col_index = -1

    # Находим столбец с минимальной суммой
    for j in range(cols):
        col_sum = sum(matrix[i][j] for i in range(rows))
        if col_sum < min_col_sum:
            min_col_sum = col_sum
            min_col_index = j

    return min_row_index, min_col_index

print(minimum([[7, 2, 7, 2, 8],
          [2, 9, 4, 1, 7],
          [3, 8, 6, 2, 4],
          [2, 5, 2, 9, 1],
          [6, 6, 5, 4, 5]]))
