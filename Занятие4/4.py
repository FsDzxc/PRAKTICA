# -- coding: utf-8 --
s = 0
n = int(input('Количество чисел: '))
for i in range(n):
    a = int(input(f'Число №{i+1}: '))
    s += a
print(s)
