class Transaction:

    def deposit_money(self, account, amount):
        if account.deposit(amount):
            print("Amount Deposited Successfully")
        else:
            print("Invalid Amount")

    def withdraw_money(self, account, amount):
        if account.withdraw(amount):
            print("Amount Withdrawn Successfully")
        else:
            print("Insufficient Balance or Invalid Amount")

    def check_balance(self, account):
        print("Current Balance:", account.get_balance())