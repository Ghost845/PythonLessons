# 1. Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента. Use comprehension.
# in
# 9

# out
# [15, 16, 2, 3, 1, 7, 5, 4, 10]
# [16, 3, 7, 10]

# in
# 10

# out
# [28, 20, 10, 5, 1, 24, 7, 15, 23, 25]
# [24, 15, 23, 25]


from random import randint


def fill_list(x: int, list1: list):
    for i in range(0, x):
        list1.append(randint(1, 50))
    return list1


list1 = []
print(fill_list(int(input('Введите количество элементов списка: ')), list1))
print([list1[i] for i in range(1, len(list1)) if list1[i] > list1[i - 1]])
