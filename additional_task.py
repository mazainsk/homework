# задан список, состоящий из списков оценок для каждого ученика в алфавитном порядке
from functools import reduce

grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
# задано множество - неупорядоченная последовательность имён всех учеников в классе
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
# ЗАДАЧА: получить словарь, где ключом будет имя ученика, а значением - его средний балл

# РЕШЕНИЕ:
students = sorted(students) # получаем сортированный список имён учеников
grades = list(map(lambda x: sum(x)/len(x), grades)) # модифицируем список, вычисляя средний балл из списка оценок каждого ученика
my_dict = dict(zip(students, grades)) # объединяем два списка в требуемый словарь
print('Результирующий словарь, где ключом каждого элемента является имя ученика, а значением - его средний балл:\n',
      my_dict)
best_student = reduce(lambda a,b: a if (a > b) else b, my_dict)
print('Лучший ученик по среднему баллу - ', best_student, ': ', my_dict[best_student], sep='')