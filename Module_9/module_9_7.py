# Домашнее задание по теме "Декораторы"

def is_prime(func):
    def wrapper(*args):
        check_func = lambda n: n > 1 and all(n % i != 0 for i in range(2, int(n ** 0.5) + 1))
        print(f'{'Простое' if check_func(func(*args)) else 'Составное'}')
        return func(*args)
    return wrapper

def is_even(func):
    def wrapper(*args):
        orig_f = func(*args)
        print(f'{'Четное' if not (orig_f % 2) else 'Нечетное'}, знаков {len(str(orig_f))}')
        return orig_f
    return wrapper

# Применение декоратора is_prime (и опционально - is_even) для обертывания функции sum_three
@is_even
@is_prime
def sum_three(num_1, num_2, num_3):
    return sum((num_1, num_2, num_3))


# Проверка на тестовых данных:
res = sum_three(2, 3, 6)    # 11 - число нечетное, знаков 2, простое
print(res)
res = sum_three(108, 4, 14)   # 126 - число четное, знаков 3, составное
print(res)