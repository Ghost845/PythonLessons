# 3. Написать функцию, аргументы имена сотрудников, возвращает словарь, ключи — первые буквы имён, значения — списки, содержащие имена, начинающиеся с соответствующей буквы.
# in
# "Иван", "Мария", "Петр", "Илья", "Марина", "Петр", "Алина", "Бибочка"

# out

# {'А': ['Алина'], 'Б': ['Бибочка'], 'И': ['Иван', 'Илья'], 'М': ['Марина', 'Мария'], 'П': ['Петр', 'Петр']}


def dictionary_create(*args):
    workers_dictionary = {}
    for i in sorted(args):
        letter = i[0]
        if letter not in workers_dictionary:
            workers_dictionary[letter] = [i]
        else:
            workers_dictionary[letter] += [i]
    return workers_dictionary


print(dictionary_create("Иван", "Мария", "Петр",
      "Илья", "Марина", "Петр", "Алина", "Бибочка"))
