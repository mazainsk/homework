# Домашнее задание по теме "Блокировки и обработка ошибок"

import random
import time
import threading


class Bank:
    """Класс для симуляции операций с банковским счетом, используя операции пополнения и снятия как отдельные потоки"""

    _balance: int = 0           # Текущий баланс счета
    _lock = threading.Lock()    # Объект-замок для блокировки потоков
    _max_operations: int = 100  # Максимальное количество успешных транзакций, отдельно для каждого вида
                                    # операций (пополнения, снятия)
    _pause: float = 0.05        # значение задержки в секундах для имитации времени выполнения операций

    # Метод совершает 100 транзакций пополнения средств
    def deposit(self):
        for deposit_count in range(self._max_operations):
            with self._lock:
                increment = random.randint(50, 500)
                self._balance += increment
                print(f'Пополнение №{deposit_count + 1}: {increment}. Баланс: {self._balance}')
                time.sleep(self._pause)

    # Метод совершает 100 транзакций снятия средств
    def take(self):
        for take_count in range(self._max_operations):
            with self._lock:
                decrement = random.randint(50, 500)
                print(f'Запрос №{take_count + 1} на {decrement}')
                if decrement > self._balance:
                    print('Запрос отклонён, недостаточно средств')
                else:
                    self._balance -= decrement
                    print(f'Снятие: {decrement}. Баланс: {self._balance}')
                time.sleep(self._pause)


bk = Bank()
# Т.к. методы Bank.deposit и Bank.take принимают self,
# в потоки в качестве аргумента нужно передать сам объект bk класса Bank
th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))
th1.start()
th2.start()
th1.join()
th2.join()
print(f'Итоговый баланс: {bk._balance}')