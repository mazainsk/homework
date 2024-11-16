# Домашнее задание по теме "Зачем нужно наследование"

class Animal:
    def __init__(self, name: str):
        self.name = name
        self.alive = True   # живой
        self.fed = False    # не накормлен, т.е. голодный

    def __str__(self):
        text = f'Имя: {self.name}, Статус: '
        text += 'живой, ' if self.alive else 'мертвый, '
        text += 'сытый' if self.fed else 'голодный'
        return text

class Plant:
    def __init__(self, name: str):
        self.name = name
        self.edible = False  # съедобность

    def __str__(self):
        text = f'Имя: {self.name}, Статус: '
        text += 'съедобный' if self.edible else 'не съедобный'
        return text

class Mammal(Animal):
    def eat(self, food: Plant): # специально в параметре показываю, что еда должна быть класса Plant
        if food.edible:
            print(f'{self.name} съел {food.name}')
            self.fed = True         # наелся
        else:
            print(f'{self.name} не стал есть {food.name}')
            self.alive = False      # гибнет от несъедобного растения, т.к. не насытился

class Predator(Animal):
    def eat(self, food: Mammal):    # специально в параметре показываю, что еда должна быть класса Mammal
        if hasattr(food, 'alive') and food.alive:
            print(f'{self.name} съел {food.name}')
            self.fed = True         # наелся
            food.alive = False      # травоядное отдало жизнь в качестве еды
        else:
            print(f'{self.name} не стал есть {food.name}')
            self.alive = False      # гибнет от несъедобного мёртвого травоядного животного, т.к. не насытился

class Flower(Plant):
    pass        # просто заглушка, потому что все атрибуты и методы аналогичны родительскому классу

class Fruit(Plant):
    def __init__(self, name):
        super().__init__(name)      # по условию задачи имя определено в родительском классе, поэтому так.
        self.edible = True          # переопределить съедобность родительского класса


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