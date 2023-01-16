import view
import model
import logg


def calculate():
    logg.write_log(logg.t(), 'Начало работы')
    num_type = view.ask_num_type()
    if num_type == 1:
        type_operation = view.ask_operation_ratio()
        match type_operation:
            case '1': func = model.sum
            case '2': func = model.sub
            case '3': func = model.mult
            case '4': func = model.div
            case '5': func = model.sqrt
            case '6': func = model.pow
            case '7': func = model.whole_div
            case '8': func = model.tile_div
            case '0':
                logg.write_log(logg.t(), 'Завершение работы')
                exit()
        oper_chars = ('+', '-', '*', '/', '√', '**', '//', '%')
        value_a = view.get_value_a()
        logg.write_log(logg.t(), f'Первое число - {value_a}')
        if type_operation == '5':
            view.write_console(f'{oper_chars[int(type_operation)-1]}{value_a} = {func(value_a)}')
            logg.write_log(logg.t(),oper_chars[int(type_operation)-1], value_a, '\t=\t', func(value_a))
            return
        else:
            while True:
                try:
                    value_b = view.get_value_b()
                    logg.write_log(logg.t(), f'Второе число - {value_b}')
                    view.write_console(value_a, oper_chars[int(type_operation)-1], value_b, ' = ', func(value_a, value_b))
                    logg.write_log(logg.t(),value_a, oper_chars[int(type_operation)-1], value_b, '\t=\t', func(value_a, value_b))
                    break
                except ZeroDivisionError:
                    logg.write_log(logg.t(),  'Ошибка ввода значения')
                    print('На ноль делить нельзя. Введите другое число!')
        return
    else:
        type_operation = view.ask_operation_complex()
        match type_operation:
            case '1': func = model.sum
            case '2': func = model.sub
            case '3': func = model.mult
            case '4': func = model.div
            case '5': func = model.sqrt
            case '6': func = model.pow
            case '0':
                logg.write_log(logg.t(), 'Завершение работы')
                exit()
        oper_chars = ('+', '-', '*', '/', '√', '**')
        complex_value_a = view.get_complex_value_a()
        logg.write_log(logg.t(), f'Первое число - {complex_value_a}')
        if type_operation == '5':
            view.write_console(f'{oper_chars[int(type_operation)-1]}{complex_value_a} = {func(complex_value_a)}')
            logg.write_log(logg.t(),oper_chars[int(type_operation)-1], complex_value_a, '\t=\t', func(complex_value_a))
            return
        else:
            while True:
                try:
                    complex_value_b = view.get_complex_value_b()
                    logg.write_log(logg.t(), f'Второе число - {complex_value_b}')
                    view.write_console(complex_value_a, oper_chars[int(type_operation)-1], complex_value_b, ' = ', func(complex_value_a, complex_value_b))
                    logg.write_log(logg.t(),complex_value_a, oper_chars[int(type_operation)-1], complex_value_b, '\t=\t', func(complex_value_a, complex_value_b))
                    break
                except ZeroDivisionError:
                    logg.write_log(logg.t(),  'Ошибка ввода значения')
                    print('На ноль делить нельзя. Введите другое число!')
        return
