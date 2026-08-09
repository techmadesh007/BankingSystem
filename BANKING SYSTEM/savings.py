from account import Account


class SavingsAccount(Account):

    def account_type(self):
        return "Savings Account"

    def withdraw(self, amount):
        if amount > 0 and amount <= self.get_balance():
            return super().withdraw(amount)
        return False
