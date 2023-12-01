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

def read_matrix_from_file(filename):
    with open(filename, 'r') as file:
        matrix = [[int(num) for num in line.split()] for line in file]
    return matrix

def write_result_to_file(filename, result):
    with open(filename, 'w') as file:
        if result:
            file.write(' '.join(map(str, result)))
        else:
            file.write("No rows with all odd elements found in the matrix.")

input_filename = "Жаров_Никита_Александрович_У-232_vvod_t2.txt"
output_filename = "Жаров_Никита_Александрович_У-232_vivod_t2.txt"
matrix = read_matrix_from_file(input_filename)
max_sum_row = find_max_sum_row(matrix)
write_result_to_file(output_filename, max_sum_row)