nickname_min_length = 3
nickname_max_length = 32

def input_nickname(min_len=3):
    """
    Функция вводит с консоли имя пользователя и проверяет его на соответствие требованию минимальной длины,
    а также обязательному наличию латинской буквы в качестве первого символа.
    :param min_len: 3-32 (необязательный)
    :return: 'Error' - если переданный параметру min_len аргумент - вне допустимого диапазона или не является числом;
             <Имя пользователя> - если введенный nickname подходящий.
    """
    if not min_len.is_integer():    # переданный аргумент - не число
        return 'Error'
    if min_len < nickname_min_length or min_len > nickname_max_length: # переданный аргумент - число, но меньше
        return 'Error'                          # минимально допустимого значения или больше максимально допустимого
    # регулярное выражение для проверки соответствия требованию:
    r_text = r'^[a-zA-Z]\w{' + str(min_len - 1) + r',}'
    while True:
        nickname = input('Имя пользователя >> ')
        nn_match = re.search(r_text, nickname)
        if nn_match is None:
            print(f'Ошибка:\n    имя должно начинаться с буквы и содержать минимум {min_len} '
                  f'символ{EON_dict.get('символ')[int(str(min_len)[-1])]}\nПовторите ввод:')
            continue
        else:
            break
    return nickname

def input_password(min_len=8):
    """
    Функция вводит с консоли пароль и проверяет его на соответствие требованию минимальной длины,
    обязательному наличию хотя бы одной латинской буквы в верхнем и нижнем регистре,
    наличию хотя бы одной цифры и одного спецсимвола.
    :param min_len >= 8 (необязательный)
    :return: 'Error' - если переданный параметру min_len аргумент - вне допустимого диапазона или не является числом;
             <пароль> - если введенный password подходящий.
    """
    if not min_len.is_integer():    # переданный аргумент - не число
        return 'Error'
    if min_len < 8:                 # переданный аргумент - число, но меньше минимально допустимого значения
        return 'Error'
    while True:
        password = input('Пароль >> ')
        pass_valid = all(re.search(i, password) for i in (r'[A-Z]', r'\d', r'[a-z]', r'[!@#$%^&*_]'))
        if not pass_valid:
            print(f'Пароль не соответствует требованиям:\n    должен состоять минимум из {min_len} '
                  f'символов,\n    содержать буквы латинского алфавита в разных регистрах, хотя бы одну цифру и '
                  f'спецсимвол из !@#$%^&*_\nПовторите ввод.')
            continue
        else:
            break
    return password