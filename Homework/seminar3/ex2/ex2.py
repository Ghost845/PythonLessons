# 2. Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# in
# 4

# out
# [2, 5, 8, 10]
# [20, 40]

# in
# 5

# out
# [2, 2, 4, 8, 8]
# [16, 16, 4]

import random
print('Введите количество элементов списка: ')
count_num = int(input())
list_1 = []
list_2 = []



def fillList(count_num):
    for i in range(count_num):
        list_1.append(random.randint(0, 11))
    return list_1

print(fillList(count_num))
list_length = len(list_1)

for k in range(list_length // 2):
    list_2.append(list_1[k] * list_1[list_length - k - 1])
if list_length % 2:
    list_2.append(list_1[list_length // 2])


print(list_2)