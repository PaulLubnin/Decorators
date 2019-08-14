import datetime

print('\n Польская нотация. \nПример ввода оператора и операндов: + 2 2')

# декоратор
def logger(path):
    def log(some_function):
        def new_function(*args, **kwargs):
            result = some_function(*args, **kwargs)
            with open(path, 'a', encoding='utf8') as file:
                file.write(f'\nВремя вызова функции: {datetime.datetime.now()}\n'
                           f'Название функции: {some_function.__name__}\n'
                           f'Аргументы с которыми вызывалась: {args, kwargs}\n'
                           f'Функция возвращает: {result}\n')
            return result
        return new_function
    return log

@logger('logs.txt')
def polish_notation(operand):
    operand_list = operand.split(' ')
    assert len(operand_list) <= 3, 'Должен быть 1 оперотор и 2 операнда!'
    assert operand_list[0] == '+' or operand_list[0] == '-' or operand_list[0] == '*' or operand_list[0] == '/',\
        'Не подходящий операнд!'
    try:
        if operand_list[0] == '+':
            print(f'Ответ: {operand_list[1]} + {operand_list[2]} = {int(operand_list[1]) + int(operand_list[2])}')
        if operand_list[0] == '-':
            print(f'Ответ: {operand_list[1]} - {operand_list[2]} = {int(operand_list[1]) - int(operand_list[2])}')
        if operand_list[0] == '/':
            print(f'Ответ: {operand_list[1]} / {operand_list[2]} = {int(operand_list[1]) / int(operand_list[2])}')
        if operand_list[0] == '*':
            print(f'Ответ: {operand_list[1]} * {operand_list[2]} = {int(operand_list[1]) * int(operand_list[2])}')
    except Exception as e:
        print(f'{type(e)},{e}')


if __name__ == '__main__':
    polish_notation(input('Введите оператора и операндов через пробел: '))
