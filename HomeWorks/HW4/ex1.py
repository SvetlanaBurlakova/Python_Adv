"""
Напишите функцию для транспонирования матрицы
"""
def transported_matrix(matrix: list) -> list:
    """Возвразает транспонированную матрицу"""
    return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]


if __name__ == '__main__':
    matrix = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]]

    for row in transported_matrix(matrix):
        print(row)
        