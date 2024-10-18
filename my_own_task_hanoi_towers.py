import time


def update_tower():
    # ф-ция перерисовывает положение дисков на осях
    global space_char
    for i in range(dm):
        tower[i] = [space_char] * 3
    tower[dm - 1][disk[dm - 1]] = str(dm) # самый большой диск всегда на нижнем уровне башни
    for i in range(dm - 2, -1, -1): # цикл по дискам, начиная со второго, по убыванию размера-индекса
        for j in range(dm - 1, -1, -1): # цикл по уровням башни, начиная с самого нижнего, с индексом (dm -1)
            if tower[j][disk[i]] == '.':
                tower[j][disk[i]] = str(i + 1)
                break
    for i in tower:
        print(*i)
    print()

# Ввод количества дисков.
while True:
    try:
        dm = int(input('Задайте количество дисков (от 1 до 8): '))
        if 8 >= dm >= 1:
            break
    except ValueError:
        print('', end='')
    print('Неверное значение, повторите ввод')
max_nodes = (1 << dm) - 1   # Общее кол-во ходов - вершин двоичного дерева
space_char = '.'
disk = []      # список номеров осей, на которых находятся диски (слева направо от 0 до 2), индекс списка - номер диска
tower = []     # список "изображений слоев": кол-во слоев по числу дисков, кол-во элементов в слое - 3 (по числу осей)
nodes = []
for i in range(dm): # инициализация положения дисков на осях
    disk.append(0)
for i in range(dm): # инициализация осей башни без учета дисков
    tower.append([space_char] * 3)
print('Число ходов для решения задачи с количеством дисков', dm, 'шт. =', max_nodes)
print('Вид Ханойской Башни с начальным положением дисков на трёх осях (стержнях):')
print()
update_tower()
# time.sleep(2)

step = max_nodes        # Номер шага, до которого показать перемещения.
root_node = 1 << (dm - 1)   # Номер корневой вершины в дереве
cur_node = root_node       # номер искомой вершины в дереве
# Определить номера осей для каждой вершины в дереве.
for i in range(max_nodes):  # инициализация массива-списка (по кол-ву ходов) из троек чисел:
    nodes.append([0] * 3)   # 1 - номер диска, 2 - номер оси, откуда перемещается диск, 3 - номер оси, куда.
for node in range(1, step + 1):
    a = 1   # номер оси, с которой перемещается текущий диск
    b = 2   # номер оси, на которую перемещается текущий диск
    # Начальная позиция поиска соответствует корневой вершине.
    cur_node = root_node
    # Изменение номера вершины при переходе к следующему поддереву.
    ind = root_node // 2
    # Двоичный поиск нужной вершины.
    while node != cur_node:
        if node < cur_node:
            # Искомая вершина в левом поддереве.
            b = 6 - a - b
            cur_node -= ind  # Переход к левому поддереву.
        else:
            # Искомая вершина в правом поддереве.
            a = 6 - a - b
            cur_node += ind  # Переход к правому поддереву.
        # Разница в номерах вершин при переходе к следующему поддереву уменьшается в два раза.
        ind //= 2
    # Номера осей для рассматриваемой вершины (текущего хода) определены.
    # Вычисление номера перемещаемого диска
    i = 0
    j = node
    while j % 2 == 0: # на нечетных ходах всегда перемещается самый маленький диск (i=0), на четных номер диска
        # вычисляется как количество делений без остатка номера хода на 2
        j //= 2
        i += 1
    # disk[i] = b - 1 # изменение положения диска i (b - ось, куда переместился диск)
    # print(f'Ход {node}: диск {i + 1}: ось {a} --> {b}:')
    nodes[node - 1] = [i, a - 1, b - 1]
    # update_tower()
    # if node < step:
    #     time.sleep(2)
# Ввод номера шага для просмотра состояния башни.
while True:
    try:
        step = int(input(f'Задайте номер шага (от 0 до {max_nodes}): '))
        if max_nodes >= step >= 0:
            break
    except ValueError:
        print('', end='')
    print('Неверное значение, повторите ввод')
# Формирование вида башен для конкретного хода
find_flags = list([False] * dm)     # Инициализация списка флагов по количеству дисков - это признаки "ход найден".
for i in range(step - 1, -1, -1):   # Начиная с номера шага просмотр предыдущих шагов, пока не будет найден последний
                                        # ход для каждого из дисков.
    if not find_flags[nodes[i][0]]: # Найден ход для диска, по которому еще не было информации.
        find_flags[nodes[i][0]] = True  # Установка флага просмотра для найденного диска.
        disk[nodes[i][0]] = nodes[i][2] # Запись номера оси, на которой находится диск.
        if all(find_flags):         # Последний ход по каждому из дисков найден.
            break
print(f'Положение дисков для хода {step}:')
print()
update_tower()
