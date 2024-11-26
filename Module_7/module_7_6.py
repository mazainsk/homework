# Домашнее задание по теме "Try и Except"

def add_everything_up2(*args):
    """
    Функция складывает числа, строки и булевы типы, учитывает вложенные списки и кортежи,
    аргументы не подходящего типа пропускаются.
    """
    values = []

    # Функция рекурсивного перестроения входных аргументов в новый ("плоский") список
    def args_remap(*args):
        nonlocal values
        for arg in args:
            if isinstance(arg, (list, tuple)):
                args_remap(*arg)
            elif isinstance(arg, (int, float, bool, str)):
                values.append(arg)

    args_remap(*args)
    result = ''
    try:
        result = sum(values)
    except TypeError:
        result = ''.join(str(i) for i in values)
    finally:
        return result


# Проверка на тестовых данных:

print(add_everything_up2(123.456, 'строка'))
print(add_everything_up2('яблоко', 4215, '_против_груши', 48.2))
print(add_everything_up2(123.456, 7))
print(add_everything_up2(5, False, True))
print(add_everything_up2(64.8, [1, 2, 3, ('?', {17, '0'}), 90], False))
print(add_everything_up2('1', {'abc'}, '?'))
