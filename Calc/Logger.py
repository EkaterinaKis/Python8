def log_exec(expr, result):
    """Записывает в файл результат исчеслений:  задача -> ответ"""
    with open('newfile.txt', 'a') as file:
        file.write(f'expr: {expr}; result: {result}\n')


def get_history():
    with open('newfile.txt', 'r') as file:
        return file.read()
