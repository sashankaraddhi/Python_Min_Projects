# Math Quiz Game

A simple **Command-Line Math Quiz Game** built with Python that tests a user's arithmetic skills through randomly generated questions. Players can choose the type of questions, difficulty level, and the number of questions they want to answer.

This project is perfect for beginners who want to practice Python concepts such as functions, loops, random number generation, exception handling, and program flow.

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

The **Math Quiz Game** is a menu-driven Python application that generates random arithmetic questions based on the user's preferences. Users can select the operation type, difficulty level, and the number of questions before starting the quiz.

The application checks each answer immediately and displays the final score at the end of the quiz.

---

# Features

* Addition Quiz
* Subtraction Quiz
* Multiplication Quiz
* Mixed Question Mode
* Five Difficulty Levels
* Custom Number of Questions
* Instant Correct/Incorrect Feedback
* Final Score Summary
* Input Validation with Exception Handling
* Interactive Command-Line Interface

---

# Technologies Used

* Python 3
* Random Module
* Functions
* Loops
* Conditional Statements
* Exception Handling (`try` / `except`)
* User Input Handling

---

# How It Works

### 1. Select Question Type

Choose one of the following quiz modes:

* Addition
* Subtraction
* Multiplication
* Mix (Randomly selects question types)

---

### 2. Choose Difficulty Level

Select a difficulty level between **1** and **5**.

Higher difficulty levels generate larger random numbers, making the quiz more challenging.

---

### 3. Enter Number of Questions

Specify how many questions you want to answer.

If an invalid value is entered, the program defaults to **10 questions**.

---

### 4. Solve the Questions

The application generates random operands based on the selected difficulty level and asks arithmetic questions one at a time.

Immediate feedback is displayed after every answer.

---

### 5. View Final Score

After completing the quiz, the program displays the total number of correct answers.

---

# Usage

Run the program:

```bash id="5i4b9g"
python math_quiz.py
```

Follow the on-screen instructions:

1. Select a question type.
2. Choose a difficulty level.
3. Enter the number of questions.
4. Answer each question.
5. View your final score.

---

# Sample Output

```text id="d9e1fh"
Choose a question type

Addition, Subtraction, Multiplication, Mix

Enter choice: Mix

How many questions? 5

Choose a level from 1-5: 3

Question 1
What is 24 plus 17?
41

Correct!

Question 2
What is 18 multiplied by 5?
90

Correct!

Question 3
What is 30 minus 14?
15

Sorry, Incorrect.

Quiz finished with 2 correct answers out of 5 questions.
```

---

# Concepts Covered

This project demonstrates:

* Functions
* Random Number Generation
* Loops (`for` and `while`)
* Conditional Statements
* Lists
* User Input Validation
* Exception Handling
* Boolean Logic
* Modular Programming

---

# Future Enhancements

Possible improvements include:

*  Division Questions
*  Timed Quiz Mode
*  High Score Tracking
*  Save Scores to a File
*  Difficulty that Increases Automatically
*  Lives System
*  Sound Effects
*  GUI Version using Tkinter
*  Web Version using Flask
*  Detailed Quiz Statistics
*  Review Incorrect Answers at the End

---

# 👨‍💻 Author

**Sashank Araddhi**

GitHub: https://github.com/sashankaraddhi


⭐ **If you found this project useful, consider giving it a star on GitHub!**
