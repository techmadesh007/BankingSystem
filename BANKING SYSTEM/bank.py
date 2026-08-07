class Bank:

    def __init__(self):
        self.accounts = []

    def add_account(self, account):
        self.accounts.append(account)

    def find_account(self, account_no):
        for account in self.accounts:
            if account.get_account_no() == account_no:
                return account
        return None

    def show_accounts(self):
        if len(self.accounts) == 0:
            print("No Accounts Available")
            return

        for account in self.accounts:
            print("\nAccount Number:", account.get_account_no())
            print("Name:", account.get_name())
            print("Account Type:", account.account_type())
            print("Balance:", account.get_balance())