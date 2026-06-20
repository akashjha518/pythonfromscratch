## Task 1: Calculate Factorial Using a Function

### 📖 Description

This program calculates the factorial of a number entered by the user
using a custom function.

The factorial of a number `n` (written as `n!`) is:

n! = n × (n-1) × (n-2) × ... × 1

### 💻 Source Code

``` python
# Calculate Factorial Using a Function
def factorial(a):
    f = 1
    for i in range(a, 1, -1):
        f *= i
    return f

num = int(input("Enter the number to find it's factorial: "))
print(f"The factorial of {num}! is {factorial(num)}")
```

------------------------------------------------------------------------
### 🔹 Output
``` bash

Enter the number to find it's factorial: 5

The factorial of 5! is 120

```
------------------------------------------------------------------------

## Task 2: Using the Math Module for Calculations

### 📖 Description

This program asks the user for a number and calculates:

-   Square root\
-   Natural logarithm (log base e)\
-   Sine (in radians)

It uses Python's built-in `math` module.

### 💻 Source Code

``` python
import math

# 1. Ask the user for a number
num = float(input("\nEnter a number: "))

# 2. Perform calculations using the math module
square_root = math.sqrt(num)
n_log = math.log(num)
sine_value = math.sin(num)

# 3. Display the results
print(f"\nResults: \nSquare root: {square_root} \nNatural logarithm (base e): {n_log} \nSine (in radians): {sine_value}\n")
```

------------------------------------------------------------------------
### 🔹 Output
``` bash

Enter a number: 25

Results: 
Square root: 5.0 
Natural logarithm (base e): 3.2188758248682006 
Sine (in radians): -0.13235175009777303

```
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

