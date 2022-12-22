def choose():
    return input(
        'Укажите, какое действие произвести:\n'
        '1 - решаем примеры,\n2 - решаем уравнение,\n'
        '3 - упрощаем многочлен,\n4 - показать историю:\n')


def get_expr():
    return input('Введите пример: ')


def show_result(result):
    print(f'Ответ: {result}')


def show_history(history):
    print(history)


def error_mode():
    print('Данного режима нет')
