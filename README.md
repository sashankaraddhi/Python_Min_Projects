# Random Greeting Generator

A simple **Python Greeting Generator** that greets users with friendly messages. The application allows users to either receive a **random greeting** or choose a greeting from a predefined list. This project is ideal for beginners to practice Python fundamentals such as dictionaries, lists, functions, exception handling, randomization, and string formatting.

---

# Table of Contents

* Introduction
* Features
* Technologies Used
* How It Works
* Usage
* Sample Output
* Concepts Covered
* Future Enhancements
* Author

---

# Introduction

The **Random Greeting Generator** is a command-line Python application that displays personalized greetings based on the user's choice. Users can either let the program randomly select a greeting or manually choose one from a list of available greeting templates.

The project demonstrates how to work with dictionaries, random number generation, input validation, exception handling, and string formatting in Python.

---

# Features

* Accepts the user's name
* Generates a random greeting
* Allows users to choose a greeting manually
* Handles invalid input using exception handling
* Uses dictionaries to manage greeting templates
* Formats greetings with the user's name
* Simple command-line interface

---

# Technologies Used

* Python 3
* Random Module
* Dictionaries
* Lists
* Functions
* Exception Handling (`try` / `except`)
* String Formatting

---

# How It Works

### 1. Enter Your Name

The program prompts the user to enter their name. The entered name is automatically converted to title case before displaying the greeting.

### 2. Choose Greeting Style

The user can choose between:

* **Random Greeting** – The program randomly selects one of the available greeting templates.
* **Manual Selection** – The user selects a greeting by entering its corresponding number.

### 3. Input Validation

If the user enters:

* A non-numeric value
* A number outside the available options

The application automatically selects a random greeting instead of terminating.

### 4. Display Greeting

The selected greeting is formatted with the user's name and displayed on the screen.

---

# Usage

Run the program:

```bash
python greeting_generator.py
```

Follow the prompts:

1. Enter your name.
2. Choose:

   * **1** → Random Greeting
   * **2** → Select a Greeting
3. Enjoy your personalized greeting!

---

# 🖥️ Sample Output

### Random Greeting

```text
Please enter your name: Sashank
Enter 1 for a random greeting, or enter 2 to choose from a list: 1

Hi there, Sashank! It's great to see you!
```

### Manual Greeting Selection

```text
Please enter your name: Sashank
Enter 1 for a random greeting, or enter 2 to choose from a list: 2

Choose an integer between 1 & 3: 3

Greetings, Sashank! How are you doing today?
```

### Invalid Input

```text
Choose an integer between 1 & 3: 10

The value you entered is not in the dictionary, returning a random greeting.

Hello, Sashank! Welcome!
```

---

# Concepts Covered

This project demonstrates:

* Lists
* Dictionaries
* Dictionary Creation using `zip()`
* Random Module
* Functions
* User Input
* Exception Handling
* String Formatting with `.format()`
* Conditional Statements

---

# Future Enhancements

Some features that can be added include:

* Multiple Language Greetings
* Greeting Categories (Formal, Casual, Motivational)
* Time-Based Greetings (Good Morning, Good Afternoon, Good Evening)
* Birthday Greetings
* Store Custom Greetings in a JSON File
* Allow Users to Add New Greetings
* Colorful Terminal Output
* GUI Version using Tkinter
* Web Version using Flask

---

# Author

**Sashank Araddhi**

GitHub: https://github.com/sashankaraddhi
