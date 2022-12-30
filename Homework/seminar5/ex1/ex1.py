# 1. Напишите программу, удаляющую из текста все слова, содержащие "абв". В тексте используется разделитель пробел.
# in
# Number of words: 10

# out
# авб абв бав абв вба бав вба абв абв абв
# авб бав вба бав вба

# in
# Number of words: 6

# out
# ваб вба абв ваб бва абв
# ваб вба ваб бва

# in
# Number of words: -1

# out
# The data is incorrect


from random import sample


print('Number of words:')
num_of_w = int(input())


def generate_random_string(length: int, alp: str = 'абв'):
    list_1 = []
    for i in range(length):
        letters = sample(alp, 3)
        list_1.append(''.join(letters))
    return ' '.join(list_1)


some_text = str(generate_random_string(num_of_w))
print(some_text)

find_txt = "абв"
list_1 = [i for i in some_text.split() if find_txt not in i]
print(f'Результат: {" ".join(list_1)}')
