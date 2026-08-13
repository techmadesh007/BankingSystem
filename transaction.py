from dataclasses import dataclass
from datetime import datetime

from exceptions import AccountNotFoundError, InsufficientFundsError


@dataclass
class Transaction:
    transaction_type: str
    amount: float
    timestamp: datetime
    description: str
    balance_before: float
    balance_after: float


class TransactionService:
    def deposit_money(self, account, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be greater than zero")

        balance_before = account.balance

        account.deposit(amount)

        transaction = Transaction(
            transaction_type="DEPOSIT",
            amount=amount,
            timestamp=datetime.now(),
            description=f"Deposited {amount}",
            balance_before=balance_before,
            balance_after=account.balance
        )

        account.add_transaction(transaction)

        return transaction

    def withdraw_money(self, account, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be greater than zero")

        if amount > account.balance:
            raise InsufficientFundsError()

        balance_before = account.balance

        account.withdraw(amount)

        transaction = Transaction(
            transaction_type="WITHDRAW",
            amount=amount,
            timestamp=datetime.now(),
            description=f"Withdrawn {amount}",
            balance_before=balance_before,
            balance_after=account.balance
        )

        account.add_transaction(transaction)

        return transaction

    def transfer_money(self, sender, receiver, amount):
        if sender is None:
            raise AccountNotFoundError("Sender account not found")

        if receiver is None:
            raise AccountNotFoundError("Receiver account not found")

        if amount <= 0:
            raise ValueError("Transfer amount must be greater than zero")

        if amount > sender.balance:
            raise InsufficientFundsError()

        sender_balance_before = sender.balance
        receiver_balance_before = receiver.balance

        try:
            sender.withdraw(amount)

            if receiver is None:
                raise AccountNotFoundError("Receiver account not found")

            receiver.deposit(amount)

            sender_transaction = Transaction(
                transaction_type="TRANSFER_OUT",
                amount=amount,
                timestamp=datetime.now(),
                description=f"Transferred {amount} to Account {receiver.account_no}",
                balance_before=sender_balance_before,
                balance_after=sender.balance
            )

            receiver_transaction = Transaction(
                transaction_type="TRANSFER_IN",
                amount=amount,
                timestamp=datetime.now(),
                description=f"Received {amount} from Account {sender.account_no}",
                balance_before=receiver_balance_before,
                balance_after=receiver.balance
            )

            sender.add_transaction(sender_transaction)
            receiver.add_transaction(receiver_transaction)

            return sender_transaction

        except Exception:
            sender.balance = sender_balance_before
            receiver.balance = receiver_balance_before
            raise

    def reverse_last_transaction(self, account):
        if len(account.transactions) == 0:
            raise ValueError("No transaction available for reversal")

        transaction = account.transactions.pop()

        if transaction.transaction_type == "DEPOSIT":
            account.balance = transaction.balance_before

        elif transaction.transaction_type == "WITHDRAW":
            account.balance = transaction.balance_before

        elif transaction.transaction_type == "TRANSFER_OUT":
            account.balance = transaction.balance_before

        elif transaction.transaction_type == "TRANSFER_IN":
            account.balance = transaction.balance_before

        else:
            account.transactions.append(transaction)
            raise ValueError("Unsupported transaction type")

        return transaction

    def check_balance(self, account):
        return account.balance

    def show_history(self, account):
        if len(account.transactions) == 0:
            return []

        return account.transactions