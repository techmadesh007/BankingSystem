class Transaction:

    def deposit_money(self, account, amount):
        if account.deposit(amount):
            print("Amount Deposited Successfully")
            print("Current Balance:", account.get_balance())
        else:
            print("Invalid Amount")

    def withdraw_money(self, account, amount):
        if account.withdraw(amount):
            print("Amount Withdrawn Successfully")
            print("Current Balance:", account.get_balance())
        else:
            print("Insufficient Balance or Invalid Amount")

    def transfer_money(self, sender, receiver, amount):

        if amount <= 0:
            print("Invalid Amount")
            return

        if amount > sender.get_balance():
            print("Insufficient Balance")
            return

        sender.withdraw(amount)
        receiver.deposit(amount)

        sender.add_transaction(
            "Transferred " + str(amount) +
            " to Account " + str(receiver.get_account_no())
        )

        receiver.add_transaction(
            "Received " + str(amount) +
            " from Account " + str(sender.get_account_no())
        )

        print("Money Transferred Successfully")

    def check_balance(self, account):
        print("Current Balance:", account.get_balance())

    def show_history(self, account):

        print("\n========== TRANSACTION HISTORY ==========")

        transactions = account.get_transactions()

        if len(transactions) == 0:
            print("No Transactions Available")
            return

        for transaction in transactions:
            print("-", transaction)
