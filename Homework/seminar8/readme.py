employees = {} # создаешь пустой список/словарь

def add_employe(first_name: str, last_name: str):
    employees.append(first_name, last_name)
    # Реализовать создания сотрудника с его атрибутами (ФИО, номер телефона и т.д.)

def find_employers():
    return employees
    # Вывести список всех сотрудников (Возвращаешь словарь сотрудников)


def find_one_employe(id: int):
    # Обработать ошибку, если не передели id не существующего сотруднка
    res = employees.sort(id: id)
    if (res пустой) выкинуть ошибку в консоль
    #


def fired_employe(id: int)
    employees.remove(id: id)

def change_salary(id: int, amount: int)
    # найти по id и изменить зарплату 

def change_position(id: int, amount: int)
    # найти по id и изменить должность 

    # DICTIONATY


def main_menu():
    menu_dict = {'1': 'Сотрудники', '2' : 'Клиенты', '3': 'Услуги', '0': 'Выход'}
    user_choice = -1
    print('Справочники')
    print('-'*10)
    for key, value in menu_dict.items():
        print(key, ' - ', value)
    while user_choice not in menu_dict.keys():
        user_choice = input('Введите номер справочника')
    return user_choice
