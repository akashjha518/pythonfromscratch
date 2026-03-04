# Task 2: Write and Append Data to a File

from pathlib import Path

# Create output.txt in the same folder as this script.
file_path = Path(__file__).with_name("output.txt")

# Step 1: Take user input and write it to the file.
first_input = input("Enter text to write to the file: ")
with open(file_path, "w") as file:
    file.write(first_input + "\n")

# Step 2: Take additional input and append it to the same file.
second_input = input("Enter additional text to append: ")
with open(file_path, "a") as file:
    file.write(second_input + "\n")

# Step 3: Read and display the final content of the file.
print("\nFinal content of output.txt:")
with open(file_path, "r") as file:
    print(file.read(), end="")
