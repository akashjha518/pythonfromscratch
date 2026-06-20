# Files, Exceptions, and Errors in Python

## Task 1: Read a File and Handle Errors

### Objective
Read a text file named `sample.txt`, print its contents line by line, and handle the case where the file does not exist.

### Code (`Task1.py`)
```python
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
```

### Run command
```powershell
python Task1.py
```

### Output
```text
This is a sample file
This file contains multiple lines
```

## Task 2: Write, Append, and Read File Content

### Objective
Take user input and write it to `output.txt`, append additional input to the same file, then read and display the final content.

### Code (`Task2.py`)
```python
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
```

### Run command
```powershell
python Task2.py
```

### Example input
```text
Hello from write
Hello from append
```

### Output
```text
Enter text to write to the file: Hello from write
Enter additional text to append: Hello from append

Final content of output.txt:
Hello from write
Hello from append
```

## Notes
- Run commands from the `Files_Exceptions_and_Errors_in_Python` folder.
- `output.txt` is created automatically when `Task2.py` runs.
