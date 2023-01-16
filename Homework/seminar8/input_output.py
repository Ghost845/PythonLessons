from random import choice
import controller as ctrl
import os, sys


def read_init_values():
    try:
        with open('employee_names.txt', 'r', encoding='utf-8') as f1, open('client_names.txt', 'r', encoding='utf-8') as f2,\
                open('posts.txt', 'r', encoding='utf-8') as f3, open('autos.txt', 'r', encoding='utf-8') as f4,\
                open('work_types.txt', 'r', encoding='utf-8') as f5:
            employee_names_list, client_names_list = f1.readlines(), f2.readlines()
            posts_list, autos_list, work_list = f3.readlines(), f4.readlines(), f5.readlines()
            employee_names_list = list(
                map(lambda x: x.replace('\n', ''), employee_names_list))
            client_names_list = list(
                map(lambda x: x.replace('\n', ''), client_names_list))
            posts_list = list(map(lambda x: x.replace('\n', ''), posts_list))
            autos_list = list(map(lambda x: x.replace('\n', ''), autos_list))
            work_list = list(map(lambda x: x.replace('\n', ''), work_list))
    except IOError:
        print('Ошибка чтения файла')
    return employee_names_list, client_names_list, posts_list, autos_list, work_list


def phone_number_gen():
    res = '+79'
    for i in range(9):
        res += str(choice(range(9)))
    return res


def main_menu():
    menu = {'1': 'Справочник сотрудников автосервиса', '2': 'Справочник клиентов автосервиса',
            '3': 'Справочник услуг', '0': 'Выход из справочника'}
    user_choice = -1
    print('Справочники автосервиса'.upper())
    print('-'*20)
    for key, value in menu.items():
        print(key, '-', value)
    print('-'*20)
    while user_choice not in menu.keys():
        user_choice = input('Выберите справочник: ')
    return user_choice


def sub_menu(branch):
    match branch:
        case 1:
            title = 'Работа со справочником сотрудников автосервиса'.upper()
            menu = {'1': 'Показать общий список сотрудников', '2': 'Найти сотрудника', '3': 'Добавить сотрудника',
                    '4': 'Изменить сотрудника', '5': 'Удалить сотрудника', '6': 'Экспорт в xml', '7': 'Экспорт в csv', '0': 'Назад'}
        case 2:
            title = 'Работа со справочником клиентов автосервиса'.upper()
            menu = {'1': 'Показать общий список клиентов', '2': 'Найти клиента', '3': 'Добавить клиента',
                    '4': 'Изменить клиента', '5': 'Удалить клиента', '6': 'Экспорт в xml', '7': 'Экспорт в csv', '0': 'Назад'}
        case 3:
            title = 'Работа со справочником услуг автосервиса'.upper()
            menu = {'1': 'Показать общий список услуг', '2': 'Найти услугу', '3': 'Добавить услугу', '4': 'Изменить услугу',
                    '5': 'Удалить услугу', '6': 'Вывести активные услуги по клиенту', '7': 'Экспорт в xml', '8': 'Экспорт в csv', '0': 'Назад'}
    choice = -1
    print('\n'+'-'*20)
    print(title)
    print('-'*20)
    for key, value in menu.items():
        print(key, ' - ', value)
        print('-'*20)
    while choice not in menu.keys():
        choice = input('Выберите действие: ')
    return (int(choice))


def print_dict(book: dict, dict_type='', client_id=''):
    match dict_type:
        case 'employee':
            print('id|Фамилия|Имя|Отчество|Телефон|Должность|Зарплата')
        case 'client':
            print('id|Фамилия|Имя|Отчество|Телефон|Автомобиль')
        case 'work':
            print('id|Клиент|Стоимость заказа|Вид работ|Мастер')
    print('-'*20)

    if dict_type == 'work':
        if client_id == '':
            for key, value in book.items():
                client_fio = ctrl.cust_dic[int(value[0])][0]+'.'+ctrl.cust_dic[int(
                    value[0])][1][0]+'.'+ctrl.cust_dic[int(value[0])][2][0]+'.'
                empl_fio = ctrl.tech_dic[int(value[0])][0]+'.'+ctrl.tech_dic[int(
                    value[0])][1][0]+'.'+ctrl.tech_dic[int(value[0])][2][0]+'.'
                print(key, '|', client_fio, '|',
                      value[1], '|', value[2], '|', empl_fio)
        else:
            fin_price = 0
            for key, value in book.items():
                if int(value[0] == client_id):
                    fin_price += int(value[1])
                    client_fio = ctrl.cust_dic[int(value[0])][0]+'.'+ctrl.cust_dic[int(
                        value[0])][1][0]+'.'+ctrl.cust_dic[int(value[0])][2][0]+'.'
                    empl_fio = ctrl.tech_dic[int(value[0])][0]+'.'+ctrl.tech_dic[int(
                        value[0])][1][0]+'.'+ctrl.tech_dic[int(value[0])][2][0]+'.'
                    print(key, '|', value[2], '|', empl_fio)
            print(f'Итого:      {fin_price}')
    else:
        for key, value in book.items():
            print(key, '|', '|'.join(value))


def write_log(*args):
    with open(os.path.join(sys.path[0],'calc.log'), 'a', encoding='utf-8') as logfile:
        logfile.write('\t'.join(list(map(lambda x: str(x), args)))+'\n')


def input_rec(dict_type: str):
    l_name = input('Фамилия: ')
    f_name = input('Имя: ')
    m_name = input('Отчество: ')
    phone_number = input('Номер телефона: ')
    post, cost, auto = ''
    match dict_type:
        case 'emloyee':
            post = input('Должность: ')
            cost = input('Зарплата: ')
        case 'client':
            auto = input('Автомобиль: ')
    return (l_name, f_name, m_name, phone_number, post, cost, auto)


def input_work():
    while True:
        try:
            client_id = int(input('id Клиента: '))
            empl_id = int(input('id Сотрудника'))
            smtng1 = ctrl.cust_dic[client_id]
            smtng2 = ctrl.empl_dic[empl_id]
            price = int(input('Стоимость ремонта: '))
            break
        except ValueError:
            print('Нужно ввести целое число. Попробуйте ещё раз.')
        except KeyError:
            print('Такого идентификатора нет в справочнике. Попробуйте ещё раз.')
    w_type = input('Вид работ: ')
    return (client_id, price, w_type, empl_id)


def print_client_works(client_id):
    try:
        id = int(client_id)
        print_dict(ctrl.work_dic, 'work', str(id))
        return True
    except ValueError:
        return False
