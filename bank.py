from collections import defaultdict

from account import Account
from exceptions import AccountNotFoundError


class Bank:
    def __init__(self):
        self.accounts = {}
        self.customer_index = defaultdict(list)
        self.next_account_no = 1001

    def create_account(self, customer_name, initial_balance=0.0):
        if initial_balance < 0:
            raise ValueError("Initial balance cannot be negative")

        account_no = self.next_account_no
        self.next_account_no += 1

        account = Account(
            account_no=account_no,
            customer_name=customer_name,
            balance=initial_balance
        )

        self.accounts[account_no] = account
        self.customer_index[customer_name].append(account_no)

        return account

    def add_account(self, account):
        if account.account_no in self.accounts:
            return False

        self.accounts[account.account_no] = account
        self.customer_index[account.customer_name].append(account.account_no)

        if account.account_no >= self.next_account_no:
            self.next_account_no = account.account_no + 1

        return True

    def find_account(self, account_no):
        account = self.accounts.get(account_no)

        if account is None:
            raise AccountNotFoundError(account_no)

        return account

    def account_exists(self, account_no):
        return account_no in self.accounts

    def close_account(self, account_no):
        account = self.find_account(account_no)

        del self.accounts[account_no]

        customer_accounts = self.customer_index[account.customer_name]

        if account_no in customer_accounts:
            customer_accounts.remove(account_no)

        if len(customer_accounts) == 0:
            del self.customer_index[account.customer_name]

        return True

    def get_accounts_by_customer(self, customer_name):
        account_numbers = self.customer_index.get(customer_name, [])

        return [
            self.accounts[account_no]
            for account_no in account_numbers
            if account_no in self.accounts
        ]

    def get_all_accounts(self):
        return list(self.accounts.values())

    def get_account_count(self):
        return len(self.accounts)