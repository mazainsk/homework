# Задача: посчитать и вывести количество одинаковых чисел среди 3-х введённых

# ВАРИАНТ №1:
print('Введите три целых числа для их сравнения между собой.')
first = int(input('Первое число: '))
second = int(input('Второе число: '))
third = int(input('Третье число: '))
print('Количество одинаковых чисел: ', end='')  # использую ключевое слово "end=" для того, чтобы исключить
                                                # "умолчальный перевод каретки"
if first == second == third:    # проверка на условие равенства всех трех чисел между собой
    print('3')
elif first == second or first == third or second == third:  # согласно приоритету выполнения операций правая часть
    # после оператора OR вычисляется только если левое выражение ложно: в данном случае последовательно проверяется
    # на истинность любой из трех возможных вариантов (когда 2 любых из 3х чисел равны между собой)
    print('2')
else:
    print('0')
print('\n')


# ВАРИАНТ №2 (опыт 9ти модулей):
while True:
    try:
        values = [int(i) for i in input('Введите через пробел три целых числа для их сравнения между '
                                                      'собой:\n>> ').split()]
    except ValueError:
        print('Ошибка в каком-то из чисел')
    else:
        if len(values) == 3:
            unic_val_count = len(set(values))
            print(f'Количество одинаковых чисел: '
                  f'{4 - unic_val_count if unic_val_count < 3 else 3 - unic_val_count}')
            break
        print('Вы ввели неверное количество чисел')


# ВАРИАНТ №3:
# решил реализовать решение задачи, когда нужно посчитать количество повторов каждого отдельно взятого числа -
# элемента последовательности произвольной длины (в данном примере решил взять от 2х до 5ти чисел)
# и получить только уникальные числа и количество каждого из них

import collections
num_count = int(input('Введите количество целых чисел для их сравнения между собой (число от 2 до 5): '))
if num_count not in range(2, 6):
    print('Недопустимое количество!')
    exit()
list_of_numbers = []
for i in range(num_count):  # повторяем ввод чисел в диапазоне от 0 до заданного количества минус 1
    list_of_numbers.append(int(input(f'Число {i + 1} из {num_count}: ')))
count_freq = dict(collections.Counter(list_of_numbers)) # формируем словарь из пар "ключ-число: количество повторов"
print('Словарь из уникальных чисел и их количества в заданной последовательности:')
print(count_freq)