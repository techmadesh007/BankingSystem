from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class Account:
    account_no: int
    customer_name: str
    balance: float = 0.0
    transactions: list = field(default_factory=list)

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be greater than zero")

        self.balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be greater than zero")

        if amount > self.balance:
            raise ValueError("Insufficient funds")

        self.balance -= amount

    def add_transaction(self, transaction):
        self.transactions.append(transaction)

    def get_transactions(self):
        return self.transactions

    def get_account_no(self):
        return self.account_no

    def get_name(self):
        return self.customer_name

    def get_balance(self):
        return self.balance

    def account_type(self):
        return "Account"