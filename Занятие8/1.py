# -- coding: utf-8 --

# Вариант 1

import math

def square_area(side):
    return side * side

def rectangle_area(length, width):
    return length * width

def triangle_area(base, height):
    return 0.5 * base * height

def circle_area(radius):
    return math.pi * radius * radius

def main():
    print("1. Площадь квадрата")
    print("2. Площадь прямоугольника")
    print("3. Площадь треугольника")
    print("4. Площадь круга")
choice = int(input("Выберите фигуру (1.Квадрат/2.Прямоугольник/3.Треугольник/4.Круг): "))

if choice == 1:
    side = float(input("Введите длину стороны квадрата: "))
    print("Площадь квадрата: ", square_area(side))
elif choice == 2:
    length = float(input("Введите длину прямоугольника: "))
    width = float(input("Введите ширину прямоугольника: "))
    print("Площадь прямоугольника: ", rectangle_area(length, width))
elif choice == 3:
    base = float(input("Введите основание треугольника: "))
    height = float(input("Введите высоту треугольника: "))
    print("Площадь треугольника: ", triangle_area(base, height))
elif choice == 4:
    radius = float(input("Введите радиус круга: "))
    print("Площадь круга: ", circle_area(radius))
else:
    print("Ошибка ввода")

if __name__ == "__main__":
    main()