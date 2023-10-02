# -- coding: utf-8 --
a = 1
s = 0
n = int(input('Число n: '))
for i in range(1, n + 1):
    a *= i
    s += a
print(s)