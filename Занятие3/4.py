# -- coding: utf-8 --
def main(a,b,l,N):
    length = (2 * l + (2 * N - 1) * a + 2 * (N - 1) * b)
    return length
a = int(input('Растояние между рядами: '))
b = int(input('Расстояние между дырками в ряду: '))
l = int(input('Длина свободного конца шнурка: '))
N = int(input('Количество дырок в ряду: '))
print('Искомая длина шнурка: ', main(a,b,l,N))