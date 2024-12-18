# Домашнее задание по теме "Блокировки и обработка ошибок"
import random
import time
import threading


class Bank():
    balance: int = 0
    lock = threading.Lock()

    def deposit(self):
        # Совершает 100 транзакций пополнения средств
        for i in range(100):
            increment = random.randint(50, 500)
            self.balance += increment
            print(f'Пополнение №{i+1}: {increment}. Баланс: {self.balance}')
            time.sleep(0.05)    # задержка - имитация скорости времени выполнения операции пополнения средств
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()

    def take(self):
        # Совершает 100 транзакций снятия средств
        for i in range(100):
            increment = random.randint(50, 500)
            print(f'Запрос №{i+1} на {increment}')
            if increment <= self.balance:
                self.balance -= increment
                print(f'Снятие: {increment}. Баланс: {self.balance}')
            else:
                print('Запрос отклонён, недостаточно средств')
                self.lock.acquire()
            time.sleep(0.05)



bk = Bank()
# Т.к. методы Bank.deposit и Bank.take принимают self, в потоки в качестве аргумента нужно передать сам объект bk
# класса Bank
th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))
th1.start()
th2.start()
th1.join()
th2.join()
print(f'Итоговый баланс: {bk.balance}')