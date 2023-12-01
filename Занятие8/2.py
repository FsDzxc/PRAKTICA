# -- coding: utf-8 --

# Вариант 1

def calculate_sum_and_average(array):
    sum_elements = sum(array)
    average = sum_elements / len(array)
    return sum_elements, average

def main():
    array1 = [5, 8, 12, 3, 9, 6]
    array2 = [15, 4, 7, 10, 13, 2, 6]
    array3 = [11, 6, 9, 14, 3]

    sum1, avg1 = calculate_sum_and_average(array1)
    sum2, avg2 = calculate_sum_and_average(array2)
    sum3, avg3 = calculate_sum_and_average(array3)

    print("Сумма элементов первого массива:", sum1, "Среднее арифметическое первого массива:", avg1)
    print("Сумма элементов второго массива:", sum2, "Среднее арифметическое второго массива:", avg2)
    print("Сумма элементов третьего массива:", sum3, "Среднее арифметическое третьего массива:", avg3)

if __name__ == "__main__":
    main()