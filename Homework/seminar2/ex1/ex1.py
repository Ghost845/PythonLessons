# 1. Напишите программу, которая принимает на вход
# вещественное число и показывает сумму его цифр.
# Без работы с методами строк.
# in -> out
# - 6782 -> 23
# - 0.67 -> 13
# - 198.45 -> 27

print('Введите число: ')
a = float(input())

sum = 0
for i in str(a):
    if i != '.':
        sum += int(i)
print('in -> out')
print(f'- {a} -> {sum}')