import time

# функция отрисовки игрового поля
def draw_area():
    for i in area:
        print(*i)
    print()

# Функция проверки на выигрыш для заданного количества подряд идущих одинаковых символов в поле заданного размера.
def check_winner():
    string = ''     # Переменная, накапливающая последовательности значений в клетках по нужным направлениям.
    # Основной блок просмотра: все горизонтали, вертикали и две диагонали.
    for i in area:
        string = string + ''.join(i) + ' '      # Все горизонтали склеиваются в одну строку через пробел.
    for j in range(area_size):                  # В эту же строку добавляются все вертикали: во внешнем цикле меняются
        for i in range(area_size):              # столбцы, во внутреннем - собираются клетки внутри текущего столбца.
            string += ''.join(area[i][j])
        string += ' '                           # Пробел в строку после каждого просмотренного столбца.
    for i in range(area_size):                  # Добавить 1-ю диагональ (от левого верхнего угла поля вправо-вниз).
        string += ''.join(area[i][i])
    string += ' '
    for i in range(area_size - 1, -1, -1):      # Добавить 2-ю диагональ (от правого верхнего угла поля влево-вниз).
        string += ''.join(area[area_size - 1 - i][i])
    string += ' '
    # Доп.блок просмотра - для случаев, когда размер поля больше, чем выигрышная длина цепочки.
    if shifts > 0:
        for j in range(1, shifts + 1):          # Дополнительные диагонали к 1-й:
            for i in range(area_size - j):                          # - верхние-левые диагонали вправо-вниз;
                string += ''.join(area[i][i + j])
            string += ' '
            for i in range(area_size - j):                          # - нижние-левые диагонали вправо-вниз.
                string += ''.join(area[i + j][i])
            string += ' '
        for j in range(1, shifts + 1):          # Дополнительные диагонали ко 2-й:
            for i in range(area_size - 1, j - 1, -1):               # - верхние-правые диагонали влево-вниз;
                string += ''.join(area[area_size - 1 - i][i - j])
            string += ' '
            for i in range(area_size - 1, j - 1, -1):               # - нижние-правые диагонали влево-вниз.
                string += ''.join(area[area_size - i + j - 1][i])
            string += ' '
    # Проверка на наличие выигрышной цепочки.
    if string.count('X' * win_length) > 0:      # Обнаружена цепочка крестиков длиной win_length.
        return 'tic'
    elif string.count('0' * win_length) > 0:    # Обнаружена цепочка ноликов длиной win_length.
        return 'tac'
    else:
        return 'toe'    # Цепочка нужной длины не обнаружена ни у крестиков, ни у ноликов.

# ----------------------------------------------------------------------------------------------------------------------
# НАЧАЛО
# ----------------------------------------------------------------------------------------------------------------------
print('Добро пожаловать в крестики-нолики')
print('----------------------------------')

# ввод значений: размер игрового поля и длина выигрышной цепочки одинаковых символов
while True:
    try:
        area_size = int(input('Задайте размер поля (3-5): '))
        if 5 >= area_size >= 3:
            break
    except ValueError:
        print('', end='')
    print('Неверное значение, повторите ввод')
if area_size == 3:
    win_length = 3
else:
    while True:
        try:
            win_length = int(input(f'Задайте длину выигрышной цепочки (от 3 до {area_size}): '))
            if area_size >= win_length >= 3:
                break
        except ValueError:
            print('', end='')
        print('Неверное значение, повторите ввод')
print()

shifts = area_size - win_length   # переменная количества смещений для проверки победителя
# (используется для просмотра дополнительных диагоналей, когда area_size > win_length)

# Инициализация игрового поля и его заполнение звёздочками (клетки без ходов).
area = []
for i in range(area_size):
    area.append(['*'] * area_size)

turn = 1        # Счетчик ходов.
result = ''     # Признак результата проверки последнего хода (варианты - "tic", "tac" или "toe").

while turn <= area_size ** 2:       # Максимальное кол-во возможных ходов известно и не может быть превышено.
    draw_area()
    print(f'Ход: {turn}')
    if turn % 2 == 0:
        turn_char = '0'
        print('Ходят нолики')
    else:
        turn_char = 'X'
        print('Ходят крестики')
    row = 0      # Начальные значения, заведомо выходящие за пределы поля, задаются для случаев их неправильного ввода,
    column = 0   # (см.ниже), т.к. компилятор может столкнуться с неопределенным значением в блоке finally.
    try:
        row = int(input(f'Введите номер строки (1 - верхняя, {area_size} - нижняя): '))
    except ValueError:
        row = 0
    finally:    # Блок кода, выполняющийся при любом исходе try-except выше
        if not (1 <= row <= area_size):
            print()
            print('Неверное значение, повторите ввод', '\n')
            time.sleep(1)   # Задержка 1 сек. для осознания неправильности хода.
            continue        # Возврат на начало цикла - к перерисовке поля и вводу координат хода.
    try:
        column = int(input(f'Введите номер столбца (1 - левый, {area_size} - правый): '))
    except ValueError:
        column = 0
    finally:
        if not (1 <= column <= area_size):
            print()
            print('Неверное значение, повторите ввод', '\n')
            time.sleep(1)  # Задержка 1 сек. для осознания неправильности хода.
            continue
    row -= 1    # Корректировка значений строки и столбца для правильной работы в качестве индексных переменных.
    column -= 1
    print()
    if area[row][column] != '*':
        print('Ячейка занята, сделайте ход заново', '\n')
        time.sleep(1)
        continue
    # ход был сделан правильно
    area[row][column] = turn_char   # Нужный символ заносится в игровое поле.
    result = check_winner()         # Проверка, привел ли ход к выигрышу:
    if result == 'tic':                 # да, нужная длина цепочки крестиков найдена;
        draw_area()
        print('Выиграли крестики!')
        break                           # выход из цикла "ход-проверка", т.к. игра завершена;
    elif result == 'tac':               # да, нужная длина цепочки ноликов найдена;
        draw_area()
        print('Выиграли нолики!')
        break                           # выход из цикла "ход-проверка", т.к. игра завершена.
    # Ход не привел к выигрышу, игра продолжается.
    turn += 1           # увеличение счетчика ходов и возврат к началу цикла "отрисовка поля - ход - проверка"

# Когда заполнены все клетки игрового поля или произошел досрочный выигрыш (выход по break из цикла while).
if result == 'toe':     # Если результат последнего хода не привел к выигрышу, то игра завершилась в ничью.
    draw_area()
    print('Ничья')
print('Конец игры')

