from savings import SavingsAccount
from current import CurrentAccount
from bank import Bank
from transaction import Transaction

bank = Bank()
transaction = Transaction()

while True:

    print("\n========== BANKING SYSTEM ==========")
    print("1. Create Account")
    print("2. View Accounts")
    print("3. Deposit")
    print("4. Withdraw")
    print("5. Check Balance")
    print("6. Search Account")
    print("7. Exit")
    print("====================================")

    choice = input("Enter Choice: ")

    if choice == "1":

        account_no = int(input("Enter Account Number: "))
        name = input("Enter Name: ")
        pin = input("Enter PIN: ")
        balance = float(input("Enter Initial Balance: "))

        print("\n1. Savings Account")
        print("2. Current Account")

        account_type = input("Choose Account Type: ")

        if account_type == "1":
            account = SavingsAccount(account_no, name, pin, balance)
            bank.add_account(account)
            print("Savings Account Created")

        elif account_type == "2":
            account = CurrentAccount(account_no, name, pin, balance)
            bank.add_account(account)
            print("Current Account Created")

        else:
            print("Invalid Account Type")

    elif choice == "2":
        bank.show_accounts()

    elif choice == "3":

        account_no = int(input("Enter Account Number: "))
        pin = input("Enter PIN: ")

        account = bank.find_account(account_no)

        if account and account.check_pin(pin):
            amount = float(input("Enter Amount: "))
            transaction.deposit_money(account, amount)
        else:
            print("Invalid Account Number or PIN")

    elif choice == "4":

        account_no = int(input("Enter Account Number: "))
        pin = input("Enter PIN: ")

        account = bank.find_account(account_no)

        if account and account.check_pin(pin):
            amount = float(input("Enter Amount: "))
            transaction.withdraw_money(account, amount)
        else:
            print("Invalid Account Number or PIN")

    elif choice == "5":

        account_no = int(input("Enter Account Number: "))
        pin = input("Enter PIN: ")

        account = bank.find_account(account_no)

        if account and account.check_pin(pin):
            transaction.check_balance(account)
        else:
            print("Invalid Account Number or PIN")

    elif choice == "6":

        account_no = int(input("Enter Account Number: "))

        account = bank.find_account(account_no)

        if account:
            print("\nAccount Found")
            print("Account Number:", account.get_account_no())
            print("Name:", account.get_name())
            print("Type:", account.account_type())
            print("Balance:", account.get_balance())
        else:
            print("Account Not Found")

    elif choice == "7":
        print("Thank You for Using Banking System")
        break

    else:
        print("Invalid Choice")