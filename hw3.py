class Bank:
    def __init__(self, name, balance):
        self._name = name          # защищённый атрибут
        self._balance = balance    # защищённый атрибут

    # Метод для получения имени банка
    def get_name(self):
        return self._name

    # Метод для получения баланса
    def get_balance(self):
        return self._balance

    # Метод для пополнения баланса
    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
        else:
            print("Сумма пополнения должна быть положительной.")

    # Метод для снятия средств
    def withdraw(self, amount):
        if 0 < amount <= self._balance:
            self._balance -= amount
        else:
            print("Неверная сумма для снятия.")

    # Метод moneyX для добавления средств с использованием input
    def moneyX(self):
        try:
            amount = float(input("Введите сумму для пополнения счета: "))
            if amount > 0:
                self.deposit(amount)
                print(f"Ваш новый баланс: {self.get_balance()}")
            else:
                print("Сумма пополнения должна быть положительной.")
        except ValueError:
            print("Ошибка: введите числовое значение.")

# Пример использования
bank = Bank("MyBank", 1000)
print(bank.get_name())        # Выводит: MyBank
print(bank.get_balance())     # Выводит: 1000

# Вызов метода moneyX для пополнения счета
bank.moneyX()


def _kill(self):
    self._balance = 0
    print("Баланс обнулён.")


# Метод для безопасного вызова _kill с запросом подтверждения
def kill_balance(self):
    confirm = input("Вы уверены, что хотите обнулить баланс? (да/нет): ")
    if confirm.lower() == 'да':
        self._kill()  # Внутренний вызов защищённого метода _kill
    else:
        print("Обнуление баланса отменено.")


# Пример использования
bank = Bank("MyBank", 1000)
print(bank.get_name())  # Выводит: MyBank
print(bank.get_balance())  # Выводит: 1000

