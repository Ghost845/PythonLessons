# 5. Реализуйте алгоритм перемешивания списка.
# Без функции shuffle из модуля random.
# 10
# -> [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# -> [0, 7, 6, 3, 4, 2, 9, 5, 1, 8]

count = 10
list_1 = []

for i in range(count):
    list_1.append(i)
print(f'-> {list_1}')

import random

for k in (list_1):
        temp = 0
        temp_index = (random.randint(0, 9))
        temp = list_1[temp_index]
        list_1[temp_index] = list_1[k]
        list_1[k] = temp

print(f'-> {list_1}')
