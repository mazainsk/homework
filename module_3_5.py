# Функция, которая считает произведение цифр числа рекурсивным методом
def get_multiplied_digits(number):
    str_number = str(number)
    if len(str_number) > 1:
        first = int(str_number[0])
        from_second = int(str_number[1:]) # Срез строкового представления числа со второго знака относительно текущего
                                # при преобразовании обратно в число автоматически игнорирует первые нули в срезе.
        if from_second == 0:    # Если число, переданное в функцию, заканчивается на ноль/нули,
            return first        # то прекращаем рекурсию на текущей цифре (это последняя цифра, не равная нулю).
        return first * get_multiplied_digits(from_second)
    else:
        return int(str_number)

result = get_multiplied_digits(41300200)
print(result)
        