# 3. Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности в том же порядке.
# in
# 7

# out
# [4, 5, 3, 3, 4, 1, 2]
# [5, 1, 2]

# in
# -1

# out
# Negative value of the number of numbers!
# []

# in
# 10

# out
# [4, 4, 5, 5, 6, 2, 3, 0, 9, 4]
# [6, 2, 3, 0, 9]

from random import randint
from collections import OrderedDict


def fillList(count_num):
    for i in range(count_num):
        list_1.append(randint(0, count_num))
    return list_1


def delAll(lst,a):
    r=[]
    for x in lst:
        if x != a:
            r+=[x]
    return r

def getUniq(list_1):
    if list_1 == []:
        return []
    if list_1[0] in list_1[1:]:
        return getUniq(delAll(list_1, list_1[0]))
    else:
        return [list_1[0]]+getUniq(list_1[1:])


print('Введите количество элементов списка: ')
count_num = int(input())
list_1 = []


fillList(count_num)
print(list_1)

list_2 = getUniq(list_1)
print(list_2)