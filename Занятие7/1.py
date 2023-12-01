# -- coding: utf-8 --

# Вариант 15

my_list = [1, 2, 3, 4, 3, 5, 6, 4]

duplicate_values = set([x for x in my_list if my_list.count(x) > 1])

if duplicate_values:
    print("Повторяющиеся элементы:", duplicate_values)
else:
    print("Повторяющихся элементов нет")