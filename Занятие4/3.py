# -- coding: utf-8 --
a = int(input('Число A: '))
b = int(input('Число B: '))
if a > b:
    for i in range(a, b + -1, -1):
        if i % 2 != 0:
            print(i)
else:
    print('А меньше В')