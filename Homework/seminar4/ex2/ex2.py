# 2. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

# in
# 54

# out
# [2, 3, 3, 3]

# in
# 9990

# out
# [2, 3, 3, 3, 5, 37]

# in
# 650

# out
# [2, 5, 5, 13]


def simple_nums(num):
    i = 2
    simple_num_list = []
    while i * i <= num:
        while num % i == 0:
            simple_num_list.append(i)
            num = num / i
        i = i + 1
    if num > 1:
        simple_num_list.append(int(num))
    return simple_num_list


print('Введите натуральное число: ')
num = int(input())
if num > 0:
    print(simple_nums(num))
else:
    print('Введённое число отрицательное!')