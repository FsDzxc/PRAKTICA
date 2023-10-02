# -- coding: utf-8 --
def main():
    n = int(input('Число n: '))
    m = int(input('Число m: '))
    k = int(input('Число k: '))
    if k < n * m and (k % n == 0 or k % m == 0):
        return 'Да'
    else:
        return 'Нет'
print(main())