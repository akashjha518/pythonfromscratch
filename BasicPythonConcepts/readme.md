## 📌 Task 1: Basic Mathematical Operations

### 🔹 Problem Description

Write a Python program that:

1. Takes two numbers as input from the user
2. Performs the following operations:

   * Addition
   * Subtraction
   * Multiplication
   * Division
3. Displays the result of each operation

### 🔹 Features

* Accepts decimal numbers using `float`
* Handles division by zero safely
* Displays clear output for each operation

### 🔹 Sample Code

```python
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

print("Addition:", num1 + num2)
print("Subtraction:", num1 - num2)
print("Multiplication:", num1 * num2)

if num2 != 0:
    print("Division:", num1 / num2)
else:
    print("Division: Undefined (cannot divide by zero)")
```
### 🔹 Output
<img width="1162" height="202" alt="image" src="https://github.com/user-attachments/assets/100aecfc-2ead-4bb3-9358-218c1a6077da" />

---

## 📌 Task 2: Personalized Greeting Program

### 🔹 Problem Description

Write a Python program that:

1. Takes the user's first name and last name as input
2. Concatenates them into a full name
3. Prints a personalized greeting message

### 🔹 Features

* Demonstrates string input and concatenation
* Creates a friendly personalized message
* Simple and beginner-friendly logic

### 🔹 Sample Code

```python
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")

full_name = first_name + " " + last_name
print("Hello, " + full_name + "! Welcome to Python program!")
```
### 🔹 Output
<img width="1125" height="113" alt="image" src="https://github.com/user-attachments/assets/7fc56280-a140-42f5-8984-b276c1e41970" />

---

## 🛠 Requirements

* Python 3.x

---

## ▶ How to Run

1. Make sure Python is installed on your system
2. Save the program in a `.py` file
3. Run using:

```bash
python filename.py
```

---



