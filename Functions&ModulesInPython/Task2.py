import math

# 1. Ask the user for a number
num = float(input("\nEnter a number: "))

# 2. Perform calculations using the math module
square_root = math.sqrt(num)
n_log = math.log(num)
sine_value = math.sin(num)

# 3. Display the results
print(f"\nResults: \nSquare root: {square_root} \nNatural logarithm (base e): {n_log} \nSine (in radians): {sine_value}\n")
