# -- coding: utf-8 --
def main(a,b,c):
    numbers = [a,b,c]
    return min(numbers)

a = int(input('Первое число: '))
b = int(input('Второе число: '))
c = int(input('Третье число: '))
print('Минимальное число: ', main(a,b,c))