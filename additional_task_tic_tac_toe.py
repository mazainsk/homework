import time

# функция отрисовки игрового поля
def draw_area():
    for i in area:
        print(*i)
    print()

# функция проверки на выигрыш для заданного количества подряд идущих одинаковых символов в поле заданного размера
def check_winner():
    check_1 = False     # инициализация флага проверки цепочек крестиков
    check_2 = False     # инициализация флага проверки цепочек ноликов
    # проверка всех возможных горизонталей
    for m in range(area_size - win_length + 1):     # смещение блока проверки по строкам
        for n in range(area_size - win_length + 1): # смещение блока проверки по столбцам
            for j in range(win_length):             # смещение первой клетки цепочки внутри блока проверки
                check_1 = tic[j + m][n]     # значение флага из 1й клетки цепочки в поле крестиков
                check_2 = tac[j + m][n]     # значение флага из 1й клетки цепочки в поле ноликов
                for i in range(1, win_length):      # проверка всех клеток горизонтальной цепочки длиной win_length..
                    check_1 = check_1 and tic[j + m][i + n]     # ..внутри блока проверки в обеих полях
                    check_2 = check_2 and tac[j + m][i + n]
                if check_1:
                    return 'tic'    # выход из ф-ции проверки, т.к. обнаружена цепочка крестиков длиной win_length
                elif check_2:
                    return 'tac'    # выход из ф-ции проверки, т.к. обнаружена цепочка ноликов длиной win_length
    # проверка всех возможных вертикалей
    for m in range(area_size - win_length + 1):
        for n in range(area_size - win_length + 1):
            for j in range(win_length):
                check_1 = tic[m][j + n]
                check_2 = tac[m][j + n]
                for i in range(1, win_length):
                    check_1 = check_1 and tic[i + m][j + n]
                    check_2 = check_2 and tac[i + m][j + n]
                if check_1:
                    return 'tic'
                elif check_2:
                    return 'tac'
# проверка всех возможных диагоналей слева-вверху вправо-вниз ("обратные слэши")
    for m in range(area_size - win_length + 1):
        for n in range(area_size - win_length + 1):
            for j in range(area_size - win_length + 1):
                check_1 = tic[j + m][j + n]
                check_2 = tac[j + m][j + n]
                for i in range(1, win_length):
                    check_1 = check_1 and tic[j + i + m][j + i + n]
                    check_2 = check_2 and tac[j + i + m][j + i + n]
                if check_1:
                    return 'tic'
                elif check_2:
                    return 'tac'
# проверка всех возможных диагоналей справа-вверху влево-вниз ("прямые слэши")
    for m in range(area_size - win_length + 1):
        for n in range(area_size - win_length + 1):
            for j in range(area_size - win_length + 1):
                check_1 = tic[j + m][area_size - 1 - j - n]
                check_2 = tac[j + m][area_size - 1 - j - n]
                for i in range(1, win_length):
                    check_1 = check_1 and tic[j + i + m][area_size - 1 - j - i - n]
                    check_2 = check_2 and tac[j + i + m][area_size - 1 - j - i - n]
                if check_1:
                    return 'tic'
                elif check_2:
                    return 'tac'
    return 'toe'    # цепочка нужной длины не обнаружена ни у крестиков, ни у ноликов

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

# инициализация игрового поля и полей флагов
tic = []
tac = []
area = []
for i in range(area_size):
    tic.append([False] * area_size)     # поле флагов крестиков
    tac.append([False] * area_size)     # поле флагов ноликов
    area.append(['*'] * area_size)      # игровое поле

turn = 1        # счетчик ходов
result = ''     # признак результата проверки последнего хода (варианты - "tic", "tac" или "toe")

while turn <= area_size ** 2:       # максимальное кол-во возможных ходов известно и не может быть превышено
    draw_area()
    print(f'Ход: {turn}')
    if turn % 2 == 0:
        turn_char = '0'
        print('Ходят нолики')
    else:
        turn_char = 'X'
        print('Ходят крестики')
    while True:
        try:
            row = int(input(f'Введите номер строки (1 - верхняя, {area_size} - нижняя): '))
            if 1 <= row <= area_size:
                break
        except ValueError:
            print('', end='')
        print('Неверное значение, повторите ввод')
    while True:
        try:
            column = int(input(f'Введите номер столбца (1 - левый, {area_size} - правый): '))
            if 1 <= column <= area_size:
                break
        except ValueError:
            print('', end='')
        print('Неверное значение, повторите ввод')
    row -= 1    # корректировка значений строки и столбца для правильной работы в качестве индексных переменных
    column -= 1
    print()
    if area[row][column] != '*':
        print('Ячейка занята, сделайте ход заново', '\n')
        time.sleep(1)       # задержка 1 сек. для осознания неправильности хода
        continue            # возврат на начало цикла (к перерисовке поля и вводу координат хода)
    # ход был сделан правильно
    area[row][column] = turn_char   # нужный символ заносится в игровое поле
    if turn_char == 'X':            # если ходили крестики,
        tic[row][column] = True     # то заносится флаг "ход сделан" в соответствующую клетку поля флагов крестиков
    elif turn_char == '0':          # аналогично для ноликов
        tac[row][column] = True
    result = check_winner()         # проверка, привел ли ход к выигрышу
    if result == 'tic':             # да, нужная длина цепочки крестиков найдена
        draw_area()
        print('Выиграли крестики!')
        break                       # выход из цикла "ход-проверка", т.к. игра завершена
    elif result == 'tac':
        draw_area()
        print('Выиграли нолики!')
        break
    turn += 1           # увеличение счетчика ходов и возврат к началу цикла "отрисовка поля - ход - проверка"

# когда заполнены все клетки игрового поля или произошел досрочный выигрыш
if result == 'toe':     # результат последнего хода - ни у крестиков, ни у ноликов нет выигрышной цепочки
    draw_area()
    print('Ничья')
print('Конец игры')

