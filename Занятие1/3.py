# -*- coding: utf-8 -*-
age = int(input('Введите ваш возраст: '))
name = input('Введите ваше имя: ')
def check(age, name):
    if name != 'Иван':
        if age > 0 and age < 75:
            if age > 16:
                print('Поздравляем вы поступили в ВГУИТ')
            else:
                print(f'Сначала нужно окончить школу!\nВам осталось учиться: {16 - age}')
        else:
            print('Неподходящий возраст')
    else:
        print('Мы не принимаем Иванов')
check(age,name)