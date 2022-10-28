

exp = ''


def choice_calc():
    global exp
    print(f'1. Класический калькулятор')
    print(f'2. Введите полностью выражение\n')
    choice = int(input('выберите вариант: '))
    if choice == 1:
        pass
    else:
        exp = input('Введите выражение без скобок:')
        return exp


def print_result(y):
    print(exp, '=', y)
