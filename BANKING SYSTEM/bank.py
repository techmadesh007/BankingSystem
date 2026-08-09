class Bank:

    def __init__(self):
        self.accounts = []

    def add_account(self, account):
        if self.find_account(account.get_account_no()) is None:
            self.accounts.append(account)
            return True
        return False

    def find_account(self, account_no):
        for account in self.accounts:
            if account.get_account_no() == account_no:
                return account
        return None

    def delete_account(self, account_no):
        account = self.find_account(account_no)

        if account:
            self.accounts.remove(account)
            return True

        return False

    def show_accounts(self):
        if len(self.accounts) == 0:
            print("\nNo Accounts Available")
            return

        print("\n========== ALL ACCOUNTS ==========")

        for account in self.accounts:
            print("Account Number:", account.get_account_no())
            print("Name:", account.get_name())
            print("Type:", account.account_type())
            print("Balance:", account.get_balance())
            print("----------------------------------")
