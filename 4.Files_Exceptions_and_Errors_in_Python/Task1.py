# Task 1: Read a File and Handle Errors

from pathlib import Path

# Build path to sample.txt in the same folder as this script.
file_name = Path(__file__).with_name("sample.txt")

try:
    # Open the file in read mode and close it automatically after use.
    with open(file_name, "r") as file:
        # Read and print each line one by one.
        for line in file:
            print(line, end="")
except FileNotFoundError:
    # Handle the case where sample.txt is missing.
    print(f"Error: '{file_name.name}' does not exist.")

