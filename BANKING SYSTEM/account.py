from abc import ABC, abstractmethod


class Account(ABC):

    def __init__(self, account_no, name, pin, balance):
        self.__account_no = account_no
        self.__name = name
        self.__pin = pin
        self.__balance = balance
        self.transactions = []

    def get_account_no(self):
        return self.__account_no

    def get_name(self):
        return self.__name

    def check_pin(self, pin):
        return self.__pin == pin

    def get_balance(self):
        return self.__balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            self.transactions.append("Deposited: " + str(amount))
            return True
        return False

    def withdraw(self, amount):
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
            self.transactions.append("Withdrawn: " + str(amount))
            return True
        return False

    def add_transaction(self, message):
        self.transactions.append(message)

    def get_transactions(self):
        return self.transactions

    @abstractmethod
    def account_type(self):
        pass
