#  Banking System in Python

A simple **Command-Line Banking System** developed in Python that allows users to create bank accounts, deposit and withdraw money, and check account balances. This project is designed for beginners to practice Python fundamentals such as functions, dictionaries, loops, exception handling, and input validation.

---

#  Table of Contents

* Introduction
* Features
* Technologies Used
* Project Structure
* How the Application Works
* Installation
* Usage
* Sample Output
* Concepts Covered
* Future Enhancements
* Author

---

# Introduction

The Banking System is a menu-driven Python application that simulates basic banking operations. User account information is stored in memory using Python dictionaries, making it a great project for understanding data structures and program flow.

The project includes proper input validation to prevent invalid account numbers, negative transactions, and withdrawals that exceed the available balance.

---

#  Features

*  Create a new bank account
*  Automatically generate a unique 6-digit account number
*  Deposit money into an account
*  Withdraw money with insufficient balance validation
*  Check account details and current balance
*  Validate user inputs using exception handling
*  Store account information using dictionaries
*  Interactive menu-driven interface

---

#  Technologies Used

* Python 3
* Random Module
* Dictionaries
* Functions
* Loops (`while`)
* Conditional Statements
* Exception Handling (`try` / `except`)
---

#  How the Application Works

## 1. Create Account

* Prompts the user to enter their name.
* Generates a random 6-digit account number.
* Creates an account with:

  * Account Holder Name
  * Account Number
  * Initial Balance ($0)
  * Transaction History

---

## 2. Deposit Money

* Verifies that the account exists.
* Accepts a valid deposit amount.
* Updates the account balance.

---

## 3. Withdraw Money

* Verifies the account number.
* Ensures the withdrawal amount is valid.
* Prevents withdrawals exceeding the available balance.
* Updates the account balance after a successful transaction.

---

## 4. Check Balance

Displays:

* Account Holder Name
* Account Number
* Current Account Balance

---

## 5. Exit

Terminates the application safely.
---

# Usage

After running the program, the following menu appears:

1. Create Account
2. Deposit
3. Withdraw
4. Check Balance
5. Exit

Choose an option by entering its corresponding number.

---

# Sample Output


Choose one Choice:

1. Create Account
2. Deposit
3. Withdraw
4. Check Balance
5. Exit

Enter the number: 1

Enter name: John

-----Account Created------
Account Number : 482951
Account Holder : John
Balance : $0


# Concepts Covered

This project demonstrates the use of:

* Functions
* Dictionaries
* Nested Dictionaries
* Random Number Generation
* Loops
* Conditional Statements
* Exception Handling
* Input Validation
* Menu-Driven Programming

---

# Future Enhancements

Planned improvements include:

* Transaction History
* PIN Authentication
* Money Transfer Between Accounts
* Delete Account
* Save Account Data using JSON
* Database Integration (SQLite/MySQL)
* Graphical User Interface (Tkinter)
* Search Account by Name
* Interest Calculation
* Account Statements
