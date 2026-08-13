class AccountNotFoundError(Exception):
    def __init__(self, account_no):
        super().__init__(f"Account {account_no} not found")


class InsufficientFundsError(Exception):
    def __init__(self, message="Insufficient funds"):
        super().__init__(message)