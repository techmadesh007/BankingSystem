from bank import Bank
from transaction import TransactionService
from statement_service import StatementService
from benchmark import run_benchmark
from exceptions import AccountNotFoundError, InsufficientFundsError


def display_account(account):
    print("\n------------------------------")
    print(f"Account Number : {account.account_no}")
    print(f"Customer Name  : {account.customer_name}")
    print(f"Balance        : ₹{account.balance:.2f}")
    print("------------------------------")


def create_account(bank, statement_service):
    try:
        name = input("Enter customer name: ").strip()

        if not name:
            print("Customer name cannot be empty")
            return

        balance = float(input("Enter initial balance: "))

        account = bank.create_account(name, balance)

        statement_service.add_account_id(account.account_no)

        print("\nAccount created successfully")
        display_account(account)

    except ValueError as error:
        print(f"Error: {error}")


def deposit_money(bank, transaction_service, statement_service):
    try:
        account_no = int(input("Enter account number: "))
        amount = float(input("Enter deposit amount: "))

        account = bank.find_account(account_no)

        transaction = transaction_service.deposit_money(account, amount)

        statement_service.add_transaction(transaction)

        print("\nDeposit successful")
        print(f"New Balance: ₹{account.balance:.2f}")

    except AccountNotFoundError as error:
        print(f"Error: {error}")

    except ValueError as error:
        print(f"Error: {error}")


def withdraw_money(bank, transaction_service, statement_service):
    try:
        account_no = int(input("Enter account number: "))
        amount = float(input("Enter withdrawal amount: "))

        account = bank.find_account(account_no)

        transaction = transaction_service.withdraw_money(account, amount)

        statement_service.add_transaction(transaction)

        print("\nWithdrawal successful")
        print(f"New Balance: ₹{account.balance:.2f}")

    except AccountNotFoundError as error:
        print(f"Error: {error}")

    except InsufficientFundsError as error:
        print(f"Error: {error}")

    except ValueError as error:
        print(f"Error: {error}")


def check_balance(bank):
    try:
        account_no = int(input("Enter account number: "))

        account = bank.find_account(account_no)

        print(f"\nAccount Balance: ₹{account.balance:.2f}")

    except AccountNotFoundError as error:
        print(f"Error: {error}")

    except ValueError:
        print("Please enter a valid account number")


def close_account(bank, statement_service):
    try:
        account_no = int(input("Enter account number: "))

        account = bank.find_account(account_no)

        if account.balance != 0:
            print("Account cannot be closed because balance is not zero")
            return

        bank.close_account(account_no)

        statement_service.remove_account_id(account_no)

        print("Account closed successfully")

    except AccountNotFoundError as error:
        print(f"Error: {error}")

    except ValueError:
        print("Please enter a valid account number")


def transfer_money(
    bank,
    transaction_service,
    statement_service
):
    try:
        sender_no = int(input("Enter sender account number: "))
        receiver_no = int(input("Enter receiver account number: "))
        amount = float(input("Enter transfer amount: "))

        if sender_no == receiver_no:
            print("Sender and receiver cannot be the same account")
            return

        sender = bank.find_account(sender_no)
        receiver = bank.find_account(receiver_no)

        sender_transaction = transaction_service.transfer_money(
            sender,
            receiver,
            amount
        )

        statement_service.add_transaction(sender_transaction)

        receiver_transaction = receiver.transactions[-1]

        statement_service.add_transaction(receiver_transaction)

        print("\nTransfer successful")
        print(f"Sender Balance  : ₹{sender.balance:.2f}")
        print(f"Receiver Balance: ₹{receiver.balance:.2f}")

    except AccountNotFoundError as error:
        print(f"Error: {error}")

    except InsufficientFundsError as error:
        print(f"Error: {error}")

    except ValueError as error:
        print(f"Error: {error}")


def reverse_transaction(
    bank,
    transaction_service
):
    try:
        account_no = int(input("Enter account number: "))

        account = bank.find_account(account_no)

        transaction = transaction_service.reverse_last_transaction(
            account
        )

        print("\nLast transaction reversed successfully")
        print(f"Transaction Type: {transaction.transaction_type}")
        print(f"Amount: ₹{transaction.amount:.2f}")
        print(f"New Balance: ₹{account.balance:.2f}")

    except AccountNotFoundError as error:
        print(f"Error: {error}")

    except ValueError as error:
        print(f"Error: {error}")


def show_history(bank, transaction_service):
    try:
        account_no = int(input("Enter account number: "))

        account = bank.find_account(account_no)

        history = transaction_service.show_history(account)

        if not history:
            print("\nNo transactions found")
            return

        print("\n========== TRANSACTION HISTORY ==========")

        for transaction in history:
            print(
                f"{transaction.timestamp} | "
                f"{transaction.transaction_type} | "
                f"₹{transaction.amount:.2f} | "
                f"{transaction.description}"
            )

    except AccountNotFoundError as error:
        print(f"Error: {error}")

    except ValueError:
        print("Please enter a valid account number")


def find_customer_accounts(bank):
    name = input("Enter customer name: ").strip()

    accounts = bank.get_accounts_by_customer(name)

    if not accounts:
        print("\nNo accounts found for this customer")
        return

    print(f"\nAccounts belonging to {name}")

    for account in accounts:
        display_account(account)


def display_all_accounts(bank):
    accounts = bank.get_all_accounts()

    if not accounts:
        print("\nNo accounts available")
        return

    print("\n========== ALL ACCOUNTS ==========")

    for account in accounts:
        display_account(account)


def show_sorted_account_ids(statement_service):
    account_ids = statement_service.get_sorted_account_ids()

    if not account_ids:
        print("\nNo accounts available")
        return

    print("\n========== SORTED ACCOUNT IDs ==========")

    for account_no in account_ids:
        print(account_no)


def find_account_position(statement_service):
    try:
        account_no = int(input("Enter account number: "))

        left_position = statement_service.find_account_position(
            account_no
        )

        right_position = statement_service.find_right_position(
            account_no
        )

        print(f"\nbisect_left position  : {left_position}")
        print(f"bisect_right position : {right_position}")

    except ValueError:
        print("Please enter a valid account number")


def show_accounts_sorted_by_balance(bank, statement_service):
    accounts = bank.get_all_accounts()

    if not accounts:
        print("\nNo accounts available")
        return

    sorted_accounts = statement_service.get_accounts_sorted_by_balance(
        accounts
    )

    print("\n========== ACCOUNTS SORTED BY BALANCE ==========")

    for account in sorted_accounts:
        print(
            f"Account: {account.account_no} | "
            f"Name: {account.customer_name} | "
            f"Balance: ₹{account.balance:.2f}"
        )


def show_date_range_statement(statement_service):
    try:
        start_date = input(
            "Enter start date (YYYY-MM-DD): "
        ).strip()

        end_date = input(
            "Enter end date (YYYY-MM-DD): "
        ).strip()

        transactions = statement_service.get_transactions_between(
            start_date,
            end_date
        )

        if not transactions:
            print("\nNo transactions found in this date range")
            return

        print("\n========== DATE RANGE STATEMENT ==========")

        for transaction in transactions:
            print(
                f"{transaction.timestamp} | "
                f"{transaction.transaction_type} | "
                f"₹{transaction.amount:.2f} | "
                f"{transaction.description}"
            )

    except ValueError as error:
        print(f"Error: {error}")


def show_menu():
    print("\n")
    print("==========================================")
    print("          SECURE BANKING SYSTEM")
    print("==========================================")
    print("1.  Create Account")
    print("2.  Deposit Money")
    print("3.  Withdraw Money")
    print("4.  Check Balance")
    print("5.  Close Account")
    print("6.  Transfer Money")
    print("7.  Reverse Last Transaction")
    print("8.  View Transaction History")
    print("9.  Find Customer Accounts")
    print("10. Display All Accounts")
    print("11. View Sorted Account IDs")
    print("12. Find Account Position")
    print("13. View Accounts Sorted By Balance")
    print("14. View Date Range Statement")
    print("15. Run Performance Benchmark")
    print("16. Exit")
    print("==========================================")


def main():
    bank = Bank()
    transaction_service = TransactionService()
    statement_service = StatementService()

    while True:
        show_menu()

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            create_account(
                bank,
                statement_service
            )

        elif choice == "2":
            deposit_money(
                bank,
                transaction_service,
                statement_service
            )

        elif choice == "3":
            withdraw_money(
                bank,
                transaction_service,
                statement_service
            )

        elif choice == "4":
            check_balance(bank)

        elif choice == "5":
            close_account(
                bank,
                statement_service
            )

        elif choice == "6":
            transfer_money(
                bank,
                transaction_service,
                statement_service
            )

        elif choice == "7":
            reverse_transaction(
                bank,
                transaction_service
            )

        elif choice == "8":
            show_history(
                bank,
                transaction_service
            )

        elif choice == "9":
            find_customer_accounts(bank)

        elif choice == "10":
            display_all_accounts(bank)

        elif choice == "11":
            show_sorted_account_ids(
                statement_service
            )

        elif choice == "12":
            find_account_position(
                statement_service
            )

        elif choice == "13":
            show_accounts_sorted_by_balance(
                bank,
                statement_service
            )

        elif choice == "14":
            show_date_range_statement(
                statement_service
            )

        elif choice == "15":
            run_benchmark()

        elif choice == "16":
            print("\nThank you for using Secure Banking System")
            break

        else:
            print("\nInvalid choice. Please select 1-16.")


if __name__ == "__main__":
    main()