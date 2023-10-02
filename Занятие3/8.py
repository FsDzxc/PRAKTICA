# -- coding: utf-8 --
def main():
    a = int(input('Первое число: '))
    b = int(input('Второе число: '))
    c = int(input('Третье число: '))
    if a == b == c:
        return 3
    elif a == b or b == c or a == c:
        return 2
    else:
        return 0
print(main())