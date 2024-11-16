# Домашнее задание по теме "Зачем нужно наследование"

class Animal:
    def __init__(self, name: str):
        self.name = name
        self.alive = True   # живой
        self.fed = False    # не накормлен, т.е. голодный

    def __str__(self):      # как информация о себе
        text = f'Имя: {self.name}, Статус: '
        text += 'живой, ' if self.alive else 'мертвый, '
        text += 'сытый' if self.fed else 'голодный'
        return text

class Plant:
    def __init__(self, name: str):
        self.name = name
        self.edible = False  # съедобность

    def __str__(self):      # как информация о себе
        text = f'Имя: {self.name}, Статус: '
        text += 'съедобный' if self.edible else 'не съедобный'
        return text

class Mammal(Animal):
    # Магический метод __init__ полностью определен в родительском классе, поэтому при определении дочерних классов
    # он не нужен нигде, кроме Fruit (см.ниже)

    def eat(self, food: Plant): # специально в параметре показываю, что "хорошая еда" должна быть класса Plant
        if hasattr(food, 'edible') and food.edible: # задаю так, что травоядное ест только то, что съедобное
            print(f'{self.name} съел {food.name}')
            self.fed = True         # наелся
        else:
            print(f'{self.name} не стал есть {food.name}')
            self.alive = False      # гибнет от несъедобного растения, т.к. не насытился

class Predator(Animal):
    def eat(self, food: Mammal):    # специально в параметре показываю, что "хорошая еда" должна быть класса Mammal
        if hasattr(food, 'alive') and food.alive:   # задаю так, что хищник ест только то, что живое
            print(f'{self.name} съел {food.name}')
            self.fed = True         # наелся
            food.alive = False      # жизнь объекта, который съели, прекратилась
        else:
            print(f'{self.name} не стал есть {food.name}')
            self.alive = False      # гибнет от несъедобного мёртвого травоядного животного, т.к. не насытился

class Flower(Plant):
    pass        # просто заглушка, потому что все атрибуты и методы определены в родительском классе

class Fruit(Plant):
    def __init__(self, name: str):
        super().__init__(name)      # по условию задачи имя определяется через родительский класс
        self.edible = True          # переопределить съедобность, унаследованную от родительского класса


# Проверка на тестовых данных
a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')
print('Перечень всех объектов:')
print(a1, a2, p1, p2, sep='\n', end='\n'*2)
print('Прямое обращение к атрибутам:')
print(f'Значение атрибута alive для {a1.name}:', a1.alive)
print(f'Значение атрибута fed для {a2.name}:',a2.fed)
print()
a1.eat(p1)      # PyCharm предупреждает, что хищник ожидает травоядного, а его пытаются накормить цветком
a2.eat(p2)
print(f'Значение атрибута alive для {a1.name}:', a1.alive)
print(f'Значение атрибута fed для {a2.name}:',a2.fed)

# Что произошло: Хищник попытался съесть цветок и погиб, млекопитающее съело фрукт и насытилось.