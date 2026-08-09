from savings import SavingsAccount
from current import CurrentAccount
from bank import Bank
from transaction import Transaction


bank = Bank()
transaction = Transaction()


while True:

    print("\n========== BANKING MANAGEMENT SYSTEM ==========")
    print("1. Create Account")
    print("2. View All Accounts")
    print("3. Search Account")
    print("4. Deposit Money")
    print("5. Withdraw Money")
    print("6. Check Balance")
    print("7. Transfer Money")
    print("8. Transaction History")
    print("9. Delete Account")
    print("10. Exit")
    print("===============================================")

    choice = input("Enter Your Choice: ")

    if choice == "1":

        account_no = int(input("Enter Account Number: "))

        if bank.find_account(account_no):
            print("Account Number Already Exists")
            continue

        name = input("Enter Name: ")
        pin = input("Create 4 Digit PIN: ")

        if len(pin) != 4 or not pin.isdigit():
            print("Invalid PIN")
            continue

        balance = float(input("Enter Initial Deposit: "))

        print("\n1. Savings Account")
        print("2. Current Account")

        account_type = input("Choose Account Type: ")

        if account_type == "1":
            account = SavingsAccount(
                account_no, name, pin, balance
            )

        elif account_type == "2":
            account = CurrentAccount(
                account_no, name, pin, balance
            )

        else:
            print("Invalid Account Type")
            continue

        bank.add_account(account)

        print("Account Created Successfully")


    elif choice == "2":

        bank.show_accounts()


    elif choice == "3":

        account_no = int(input("Enter Account Number: "))

        account = bank.find_account(account_no)

        if account:
            print("\nAccount Found")
            print("Account Number:", account.get_account_no())
            print("Name:", account.get_name())
            print("Account Type:", account.account_type())
            print("Balance:", account.get_balance())

        else:
            print("Account Not Found")


    elif choice == "4":

        account_no = int(input("Enter Account Number: "))
        pin = input("Enter PIN: ")

        account = bank.find_account(account_no)

        if account and account.check_pin(pin):

            amount = float(input("Enter Deposit Amount: "))

            transaction.deposit_money(account, amount)

        else:
            print("Invalid Account Number or PIN")


    elif choice == "5":

        account_no = int(input("Enter Account Number: "))
        pin = input("Enter PIN: ")

        account = bank.find_account(account_no)

        if account and account.check_pin(pin):

            amount = float(input("Enter Withdrawal Amount: "))

            transaction.withdraw_money(account, amount)

        else:
            print("Invalid Account Number or PIN")


    elif choice == "6":

        account_no = int(input("Enter Account Number: "))
        pin = input("Enter PIN: ")

        account = bank.find_account(account_no)

        if account and account.check_pin(pin):

            transaction.check_balance(account)

        else:
            print("Invalid Account Number or PIN")


    elif choice == "7":

        sender_no = int(input("Enter Sender Account Number: "))
        sender_pin = input("Enter Sender PIN: ")

        sender = bank.find_account(sender_no)

        if sender and sender.check_pin(sender_pin):

            receiver_no = int(input("Enter Receiver Account Number: "))

            receiver = bank.find_account(receiver_no)

            if receiver:

                amount = float(input("Enter Transfer Amount: "))

                transaction.transfer_money(
                    sender,
                    receiver,
                    amount
                )

            else:
                print("Receiver Account Not Found")

        else:
            print("Invalid Sender Account or PIN")


    elif choice == "8":

        account_no = int(input("Enter Account Number: "))
        pin = input("Enter PIN: ")

        account = bank.find_account(account_no)

        if account and account.check_pin(pin):

            transaction.show_history(account)

        else:
            print("Invalid Account Number or PIN")


    elif choice == "9":

        account_no = int(input("Enter Account Number: "))
        pin = input("Enter PIN: ")

        account = bank.find_account(account_no)

        if account and account.check_pin(pin):

            if bank.delete_account(account_no):
                print("Account Deleted Successfully")

        else:
            print("Invalid Account Number or PIN")


    elif choice == "10":

        print("Thank You for Using Banking Management System")
        break


    else:
        print("Invalid Choice")
