## 📌 Task 1: Check if a Number is Even or Odd

### 🔹 Problem Description

Write a Python program that:

1.   Uses a for loop to iterate over numbers from 1 to 50.

2.   Calculates the sum of all integers in this range.

3.   Displays the final sum.


### 🔹 Features

* Accepts integers using `int`
* Takes user input dynamically
* Uses formatted string output (f-strings)

### 🔹 Sample Code

```python
print("\nTo find the given Integer is even/odd.\n")
num = int(input("Enter an Integer: "))

# if the remainder is 0 then it is even
if num % 2 == 0:
    print(f"\n{num} is an Even Integer\n")

# if the remainder is not 0 then it is odd
else:
    print(f"\n{num} is an Odd Integer\n")
```
### 🔹 Output


---

## 📌 Task 2: Sum of Integers from 1 to 50 Using a Loop

### 🔹 Problem Description

Write a Python program that:

1.   Uses a for loop to iterate over numbers from 1 to 50.

2.   Calculates the sum of all integers in this range.

3.   Displays the final sum.


### 🔹 Features

* Uses a for loop for iteration
* Demonstrates accumulator pattern (+=)
* Beginner-friendly and easy to understand

### 🔹 Sample Code

```python
print("\nTo find the sum of first 'n' +ve integer.\n")
num = int(input("Enter an positive Integer: ")) #Taking input from the user
sum=0
count=0
# sum of 1 to n integers
for i in range(1,num+1):
    sum +=i
    count+=1


print(f"\nThe sum of first {count} integer is {sum}.\n")

```
### 🔹 Output

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


