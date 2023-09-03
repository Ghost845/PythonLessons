# 1. Задайте список, состоящий из произвольных чисел, количество задаёт пользователь.
# Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётных позициях(не индексах).
# in
# 5

# out
# [10, 2, 3, 8, 9]
# 22

# in
# 4

# out
# [4, 2, 4, 9]
# 8

import random
print('Введите количество элементов списка: ')
count_num = int(input())
list_1 = []
sum = 0


def fillList(count_num):
    for i in range(count_num):
        list_1.append(random.randint(0, 100))
    return list_1



for i in range(0, len(list_1), 2):
    sum += list_1[i]

print(fillList(count_num))
print(sum)
