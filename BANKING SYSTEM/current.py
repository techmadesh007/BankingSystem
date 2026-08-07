from account import Account

class CurrentAccount(Account):

    def account_type(self):
        return "Current Account"

    def withdraw(self, amount):
        if amount > 0 and amount <= self.get_balance():
            return super().withdraw(amount)
        return False