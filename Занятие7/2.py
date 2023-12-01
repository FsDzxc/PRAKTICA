# -- coding: utf-8 --

# Вариант 15

original_array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
odd_array = [x for x in original_array if x % 2 != 0]

if odd_array:
    sorted_odd_array = sorted(odd_array, reverse=True)
    print("Массив из нечетных чисел в порядке убывания:", sorted_odd_array)
else:
    print("В исходном массиве нет нечетных чисел")