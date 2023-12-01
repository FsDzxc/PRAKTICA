# -- coding: utf-8 --

# Вариант 15

def find_max_sum_row(matrix):
    max_sum = 0
    max_sum_row = None

    for row in matrix:
        if all(element % 2 != 0 for element in row):
            row_sum = sum(abs(element) for element in row)
            if row_sum > max_sum:
                max_sum = row_sum
                max_sum_row = row

    return max_sum_row

# Пример использования функции
M = [[1, 3, 5], [2, -3, 7], [5, 9, -1]]
result_row = find_max_sum_row(M)
print(result_row)