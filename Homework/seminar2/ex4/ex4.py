#  4. Напишите программу, которая принимает на вход 2 числа.
# Получите значение N, для пустого списка, заполните числами в диапзоне [-N, N].
# Найдите произведение элементов на указанных позициях(не индексах).

# Enter the value of N: 5
# Position one: 1
# Position two: 2
# -> [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
# -> 20

# Enter the value of N: 4
# Position one: 20
# Position two: 22
# -> [-4, -3, -2, -1, 0, 1, 2, 3, 4]
# -> There are no values for these indexes!

print('Введите первое число: ')
a = int(input())
print('Введите второе число: ')
b = int(input())

print('Введите значение диапазона N: ')
n = int(input())
list = []
sum = 1

for i in range(-n, n + 1):
    list.append(i)

if -n < a < n and -n < b < n:
    for k in range(1, len(list)):
        if k == a:
            print(f'Position one: {list[k]}')
            sum *= list[k - 1]
        elif k == b:
            print(f'Position two: {list[k]}')
            sum *= list[k - 1]

    print(f'-> {list}')
    print(f'-> {sum}')
else:
    print(f'-> {list}')
    print(f'-> There are no values for these indexes!')
