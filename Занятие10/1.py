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

input_filename = "Жаров_Никита_Александрович_У-232_vvod_t1.txt"
output_filename = "Жаров_Никита_Александрович_У-232_vivod_t1.txt"
matrix = read_matrix_from_file(input_filename)
modified_matrix = multiply_rows_with_element(matrix, 3, 5)
write_result_to_file(output_filename, modified_matrix)