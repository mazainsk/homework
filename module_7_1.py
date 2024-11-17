# Домашнее задание по теме "Режимы открытия файлов"

import os

class Product:

    def __init__(self, name: str, weight: float, category: str):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return (', '.join([self.name, str(self.weight), self.category]))

class Shop:
    __file_name = 'products.txt'
    __is_file_exist = False

    def __init__(self):
        if os.path.isfile(self.__file_name):
            self.__is_file_exist = True

    def get_products(self):
        if self.__is_file_exist:
            with open(self.__file_name, 'r') as  file:  # в конструкции with файл закроется автоматом, без file.close()
                data_prod = file.read().splitlines()
        else:
            data_prod = []
        return data_prod

    def add(self, *products: Product):
        exist_prod = self.get_products()
        new_products = [i.__str__() for i in products]
        if exist_prod:      # какие-то данные были прочитаны из файла
            # из new_products убрать те элементы, названия продуктов в которых есть в exist_prod
            tmp_list = list(new_products)   # временная копия списка, в которой останутся лишь уникальные продукты
            for new_prod in new_products:
                name = new_prod.split(', ')[0]      # 0 - name, 1 - weight, 2 - category
                for ex_prod in exist_prod:
                    if ex_prod.startswith(name):
                        tmp_list.remove(new_prod)   # убрать элемент целиком
                        break
            if tmp_list:
                # из новых продуктов осталось что-то, чего нет в файле
                result_products = tmp_list
            else:
                # все названия продуктов уже есть в файле, запись не нужна
                return
        else:
            # продуктов в файле нет вообще, нужно записать все
            result_products = new_products
        file = open(self.__file_name, 'a')  # добавление отсутствующих продуктов
        for prod in result_products:
            file.write(prod + '\n')
        self.__is_file_exist = True
        file.close()

if __name__ == '__main__':

    # Проверка на тестовых данных, файл 'products.txt' нужно предварительно удалить!!
    s1 = Shop()
    print('Продукты, добавляемые в файл:')
    p1 = Product('Potato', 50.5, 'Vegetables')
    p2 = Product('Spaghetti', 3.4, 'Groceries')
    p3 = Product('Potato', 5.5, 'Vegetables')   # дубликат имени, но запишется отдельным элементом
    print(p1, p2, p3, sep='\n')
    print('Список из файла ДО добавления в него новых продуктов:', s1.get_products(), sep='\n')
    s1.add(p1, p2, p3)
    print('Список из файла ПОСЛЕ добавления в него новых продуктов:', s1.get_products(), sep='\n')

    print()
    print('Еще продукты, добавляемые в файл:')
    p3 = Product('Potato', 1, 'Veg')            # повтор имени, данные не добавятся
    p4 = Product('Apples', 18.1, 'Fruits')      # новый продукт, добавится
    print(p3, p4, sep='\n')
    print('Список из файла ДО добавления в него новых продуктов:', s1.get_products(), sep='\n')
    s1.add(p3, p4)
    print('Список из файла ПОСЛЕ добавления в него новых продуктов:', s1.get_products(), sep='\n')
