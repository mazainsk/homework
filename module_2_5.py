# Вариант 1 - решение строго по пунктам в описании задачи (указаны в соответствующих комментариях ниже)

def get_matrix (n, m, value):   # объявление ф-ции с нужными параметрами (п.1)
    matrix = []                 # создание пустого списка (п.2)
    for i in range(n):          # внешний цикл для кол-ва строк матрицы, n повторов (п.3)
        matrix.append([])       # добавление пустого списка (п.4)
        for j in range(m):      # внутренний цикл для кол-ва столбцов матрицы, m повторов (п.5)
            matrix[i].append(value)    # пополнение ранее добавленного пустого списка значениями value (п.6)
    return matrix               # возврат значения переменной при выходе из функции (п.7)

# проверка алгоритма на конкретном примере исходных данных
result1 = get_matrix(2, 2, 10)
result2 = get_matrix(3, 5, 42)
result3 = get_matrix(4, 2, 13)
print(result1)
print(result2)
print(result3)

# Вариант 2 - без вложенного цикла и индексной переменной
def get_matrix (n, m, value):
    matrix = []
    for _ in range(n):
        matrix.append([value] * m)
    return matrix

# проверка алгоритма на конкретном примере исходных данных
result1 = get_matrix(2, 2, 10)
result2 = get_matrix(3, 5, 42)
result3 = get_matrix(4, 2, 13)
print(result1)
print(result2)
print(result3)