import random as rd 
accounts = {}

def menu():
    chose_type = {1 : "Create Account ",
                   2 : " Deposit ", 3 : "Withdraw ",
                  4 : "Check Balance ", 5 : "Exit"}
    print(f"Chose one Choice from {chose_type} :")
    while True:
        try:
            choice = int(input("Enter the number : "))
        except ValueError:
            print("Chose a number between 1-6")
            continue

        for keys,values in chose_type.items():
            print(f"{keys}.{values}")

        if choice not in chose_type:
            print("Invalid choice ")
            continue
        print(f"you choose {chose_type[choice]} ")
        return choice

def generate_account_number():
    return rd.randint(100000,999999)

def create_account():
    while True:
        name = input("Enter name :")

        if name.isalpha() :
            print("Name can be only in Letter")

        else :
            print("Invalid Syntax")
            continue
        break

    account_number = generate_account_number()
    accounts[account_number]={
        "name" : name.title(),
        "Balance" : 0,
        "Transaction_history" : ["Account Created"]
    }
    print("-----Account Created------")
    print(f"Account Number : {account_number}")
    print(f"Account Holder : {name}")
    print(f"Balance : $0")
    print("Create Account function called")


def deposit():
    while True:
        try :
            acc_no = int(input("Enter the Account Number :"))
    
        except ValueError:
            print("Please enter the Account Number : ")
            continue

        if acc_no not in accounts:
            print("Account not Found")
            continue
        else :
            print(f"It is Valid account : {acc_no}")
        break
    while True:
        try:
            amount_deposit = int(input("Enter the Amount: "))
        except ValueError:
            print("Please enter a valid amount.")
            continue

        if amount_deposit <= 0:
            print("Amount must be greater than 0.")
            continue

        break

    accounts[acc_no]["Balance"] += amount_deposit

    print("------ Deposit Successful ------")
    print(f"Deposited: ${amount_deposit}")
    print(f"Current Balance: ${accounts[acc_no]['Balance']}")

    print("Deposit function called")


def withdraw():
    while True:
        try:
            acc_no = int(input("Enter the Account Number: "))
        except ValueError:
            print("Please enter a valid account number.")
            continue

        if acc_no not in accounts:
            print("Account not found.")
            continue

        print(f"Valid Account: {acc_no}")
        break
    while True:
        try:
            amount = int(input("Enter withdrawal amount: "))
        except ValueError:
            print("Please enter a valid amount.")
            continue

        if amount <= 0:
            print("Amount must be greater than 0.")
            continue

        # Step 3: Check Balance
        if amount > accounts[acc_no]["Balance"]:
            print("Insufficient balance.")
            continue

        break

    accounts[acc_no]["Balance"] -= amount

    print("------ Withdrawal Successful ------")
    print(f"Withdrawn: ${amount}")
    print(f"Current Balance: ${accounts[acc_no]['Balance']}")
    print("Withdraw function called")


def check_balance():
    while True:
        try:
            acc_no = int(input("Enter the Account Number: "))
        except ValueError:
            print("Please enter a valid account number.")
            continue

        if acc_no not in accounts:
            print("Account not found.")
            continue

        break

    print("------ Account Details ------")
    print(f"Account Holder : {accounts[acc_no]['name']}")
    print(f"Account Number : {acc_no}")
    print(f"Balance        : ${accounts[acc_no]['Balance']}")
    print("Check Balance function called")


def main() -> None:
    while True:
        cred = menu()
        if cred == 1:
            create_account()
        elif cred == 2:
            deposit()
        elif cred == 3:
            withdraw()
        elif cred == 4:
            check_balance()
        elif cred == 5:
            print("Thank you for choosing your Bank")
            break


if __name__ == "__main__":
    main()