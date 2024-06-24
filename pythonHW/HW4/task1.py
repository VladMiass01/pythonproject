# Напишите функцию для транспонирования матрицы transposed_matrix,
# принимает в аргументы matrix, и возвращает транспонированную матрицу.

def transpose(matrix):
    rows = len(matrix)
    columns = len(matrix[0])
    transposed = [[0] * rows for _ in range(columns)]
    for i in range(rows):
        for j in range(columns):
            transposed[j][i] = matrix[i][j]

    return transposed


matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(matrix)
transposed_matrix = transpose(matrix)
print(transposed_matrix)
