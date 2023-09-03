import logg

value_a = 0
value_b = 0
compl_value_a = 0
compl_value_b = 0


def write_console(*args):
    print(' '.join(list(map(lambda x: str(x), args))))
    return


def get_value_a():
    global value_a
    while True:
        try:
            value_a = float(input('Введите первое значение: '))
            break
        except ValueError:
            logg.write_log(logg.t(),  'Ошибка ввода значения')
            print('Нужно вводить числовое значение. Попробуйте ещё раз!')
    return value_a


def get_value_b():
    global value_b
    while True:
        try:
            value_b = float(input('Введите второе значение: '))
            break
        except ValueError:
            logg.write_log(logg.t(),  'Ошибка ввода значения')
            print('Нужно вводить числовое значение. Попробуйте ещё раз!')
        except ZeroDivisionError:
            logg.write_log(logg.t(),  'Ошибка ввода значения')
            print('На ноль делить нельзя. Введите другое число!')
    return value_b


def ask_operation_ratio():
    message2 = '''
Введите номер операции, которую вы хотите совершить и нажмите Enter:
 
1 : Сложение
2 : Вычитание
3 : Умножение
4 : Деление
5 : Квадратный корень
6 : Возведение в степень
7 : Целочисленное деление
8 : Отсаток от деления
0 : Выход

Ваш выбор:
'''
    try:
        type_operation = input(message2)
    except ValueError:
        logg.write_log(logg.t(),  'Ошибка ввода значения')
        print('Нужно вводить числовое значение в пределах от 1 до 8. Попробуйте ещё раз!')
    return type_operation


def ask_num_type():
    message1 = '''
Выберите тип чисел, с которыми будут производиться расчёты и нажмите Enter:
 
1 : Рациональные
2 : Комплексные
0 : Выход

Ваш выбор:
'''
    try:
        num_type = input(message1)
    except ValueError:
        logg.write_log(logg.t(),  'Ошибка ввода значения')
        print('Нужно вводить числовое значение в пределах от 1 до 2. Попробуйте ещё раз!')
    return num_type


def ask_operation_complex():
    message3 = '''
Введите номер операции, которую вы хотите совершить и нажмите Enter:
 
1 : Сложение
2 : Вычитание
3 : Умножение
4 : Деление
5 : Квадратный корень
6 : Возведение в степень
0 : Выход

Ваш выбор:
'''
    try:
        type_operation = input(message3)
    except ValueError:
        logg.write_log(logg.t(),  'Ошибка ввода значения')
        print('Нужно вводить числовое значение в пределах от 1 до 6. Попробуйте ещё раз!')
    return type_operation


def get_complex_value_a():
    global compl_value_a
    while True:
        try:
            a = complex(float(input('Введите действительную часть 1-го числа: ')))
            b = complex(float(input('Введите мнимую часть 1-го числа: ')))
            compl_value_a = complex(a, b)
            break
        except ValueError:
            logg.write_log(logg.t(),  'Ошибка ввода значения')
            print('Нужно вводить числовое значение. Попробуйте ещё раз!')
    return compl_value_a


def get_complex_value_b():
    global compl_value_b
    while True:
        try:
            a = complex(float(input('Введите действительную часть 2-го числа: ')))
            b = complex(float(input('Введите мнимую часть 2-го числа: ')))
            compl_value_b = complex(a,b)
            break
        except ValueError:
            logg.write_log(logg.t(),  'Ошибка ввода значения')
            print('Нужно вводить числовое значение. Попробуйте ещё раз!')
        except ZeroDivisionError:
            logg.write_log(logg.t(),  'Ошибка ввода значения')
            print('На ноль делить нельзя. Введите другое число!')
    return compl_value_b
