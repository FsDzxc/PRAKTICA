# -- coding: utf-8 --

# Вариант 15

text = str(input('Введите строку: '))
count = 0
for letter in text:
    if letter == 'т':
        count += 1
print("Количество букв 'т' в строке:", count)