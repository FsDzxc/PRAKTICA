# -- coding: utf-8 --

# Вариант 15

def multiply_rows_with_element(matrix, c, d):
    rows_to_modify = []

    for i in range(len(matrix)):
        if c in matrix[i]:
            rows_to_modify.append(i)

    for row in rows_to_modify:
        matrix[row] = [element * d for element in matrix[row]]

    return matrix

# Пример использования функции
R = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
c = 5
d = 2
result = multiply_rows_with_element(R, c, d)
print(result)