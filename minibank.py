USER_DETAILS_FILE = 'user.txt'
ACCOUNT_NUMBER_FILE = 'account_information.txt'
ADMIN_DETAILS_FILE= 'admin.txt'
ACCOUNT_DEATILS_FILE='transaction.txt'


Created_Accounts= {}
lastUserID=1

def createAccountNumber():
    defaultintial="5000"
    global lastUserID
    lastUserID += 1
    Acc_number=defaultintial+str(lastUserID)
    return Acc_number
def getDetails():
    accounttype =input("1 for login as admin\n 2 for login as member \n Enter your user type : ")
    if accounttype=="1":
        username = input("enter your user name:")
        userpassword = input ("enter your userpassword:") 
        file=open('admin.txt','a')
        file.write(f'{username}:{userpassword} \n') 
        file.write('-\n')
        file.close()
        account_create(username,userpassword)
    else:
        accounttype=="2"
        customer_login()
import random
import string

def generate_password():
    length = 4
    characters = string.ascii_letters + string.digits + string.punctuation 
    password = ''.join(random.choice(characters) for i in range(length))
    return password

def generate_username():
    customer_id = "CUST" + str(random.randint(1000, 9999))  
    return customer_id

def customer_login():
    username = generate_username()
    password = generate_password()
    
    print(f"Your Customer Username is: {username}")
    print(f"Your Customer Password is: {password}")

    input_username = input("Enter your Username: ")
    input_password = input("Enter your Password: ")
    if input_username == username and input_password == password:
        print("Login successful!")
        file=open('user.txt','a')
        file.write(f'{username}:{password} \n') 
        file.write('-\n')
        file.close()
        account_create(username,password)
        show_menu()
    else:
        print("Invalid username or password!")
        return
accounts = {}            
def account_create(username, userpassword):
    accountNumber=createAccountNumber()
    Created_Accounts[accountNumber]={
        "username" :username,
        "password": userpassword,
        "Balance" :0  
    } 
    print(f"Your account_number is {accountNumber}")
    initial_balance=float(input ("Enter ur Initial Balance"))
    if initial_balance > 0:
        Created_Accounts[accountNumber]["balance"]=initial_balance
    else:
        print("Ur initial balance will be negative")
    print(f"Ur account created successfully! your account currentbalance is {initial_balance}")
    with open('account_information.txt', 'a') as file:
        file.write(f'{lastUserID}:{accountNumber}:{Created_Accounts[accountNumber]}\n')

    accounts[accountNumber]= {"name":username,"balance":initial_balance,"transactions":[]}

import datetime
def deposit_money(account_number, amount):
    if account_number in accounts:
        if amount > 0:
            accounts[account_number]["balance"] += amount
            transaction = {
                "type": "Deposit",
                "amount": amount,
                "date":datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }
            accounts[account_number]["transactions"].append(transaction)
            print(f"Deposit of amount successful! New balance:{accounts[account_number]['balance']}")
            with open('transaction.txt', 'a') as file:
                file.write(f'{lastUserID}:{account_number}:{transaction}:\n')
        else:
            print("Error: Deposit amount must be a positive number.")
    else:
        print("Error: Account not found.")
        account_number = input("Enter account number: ")
        amount = float(input("Enter deposit amount: "))
        if account_number in accounts:
            print("\nTransaction History:")
            for transaction in accounts[account_number]["transactions"]:
                print(transaction)
            else:
                print("\nError: Account not found. Cannot display transaction history.")



import datetime
def withdraw_money(account_number, amount):
    if account_number in accounts:
        if amount > 0:
            if  accounts[account_number]['balance'] >=amount:
                accounts[account_number]['balance']-=amount
                transaction = {
                    "type": "Withdrawal",
                    "amount": amount,
                    "date":datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                }
                accounts[account_number]["transactions"].append(transaction)
                print(f"Withdrawal of amount successful! New balance:{accounts[account_number]['balance']}")
                with open('transaction.txt', 'a') as file:
                    file.write(f'{lastUserID}:{account_number}:{transaction}:\n')
            else:
                print("Error: Insufficient balance.")
        else:
            print("Error: Withdrawal amount must be a positive number.")
    else:
        print("Error: Account not found.")

        account_number = input("Enter account number: ")
        amount = float(input("Enter withdrawal amount: "))
        if account_number in accounts:
            print("\nTransaction History:")
            for transaction in accounts[account_number]["transactions"]:
                print(transaction)
        else:
            print("\nError: Account not found. Cannot display transaction history.")

def check_balance(account_number):
    if account_number in accounts:
        balance = accounts[account_number]["balance"]
        print(f" Current balance of / {account_number} / is: {balance}")
        with open('transaction.txt', 'a') as file:
                file.write(f'{lastUserID}:{account_number}:"balance"-{balance}\n')
    else:
        print("Error:account not found.")

def transaction_history(account_number):
        if account_number in accounts:
            print("\nTransaction History:")
            for transaction in accounts[account_number]["transactions"]:
                print(transaction)
        else:
            print("\nError: Account not found. Cannot display transaction history.")
def see_menu():
    while True:
        print("\nMenu:")
        print("1.Created Account")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Check Balance")
        print("5. Transcation history")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")
        if choice == '1':
            createAccountNumber()
            getDetails()
        elif choice == '2':
            account_number = input("Enter account number: ")
            amount = float(input("Enter deposit amount: "))
            deposit_money(account_number, amount)
        elif choice == '3':
            account_number = input("Enter account number: ")
            amount = float(input("Enter withdrawal amount: "))
            withdraw_money(account_number, amount)
        elif choice == '4':
            account_number = input("Enter account number: ")
            check_balance(account_number)
        elif choice == '5':
            account_number=input("Enter the account_number:")
            transaction_history(account_number)
        elif choice == '6':
            print("Thank you for using our mini bank. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")

def show_menu():
    while True:
        print("\nMenu:")
        print("1. Deposit Money")
        print("2. Withdraw Money")
        print("3. Check Balance")
        print("4. Transcation history")
        print("5. Exit")

        choice = input("Enter your choice (1-6): ")
        if choice == '1':
            account_number = input("Enter account number: ")
            amount = float(input("Enter deposit amount: "))
            deposit_money(account_number, amount)
        elif choice == '2':
            account_number = input("Enter account number: ")
            amount = float(input("Enter withdrawal amount: "))
            withdraw_money(account_number, amount)
        elif choice == '3':
            account_number = input("Enter account number: ")
            check_balance(account_number)
        elif choice == '4':
             transaction_history(account_number)
        elif choice == '5':
            print("Thank you for using our mini bank. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")

def admin_signup():
    while True:
        print("AdminSign-up")
        admin_username = "admin"
        admin_password = "admin5080"
        input_username = input("Enter Username: ")
        input_password = input("Enter Password: ")
        if input_username == admin_username and input_password == admin_password:
            print(f"Admin login successful!Welcome,{admin_username}.")
            see_menu()
        else:
            print("Admin login unsuccess,please try again")
admin_signup()