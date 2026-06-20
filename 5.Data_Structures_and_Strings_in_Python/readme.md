# Python Tasks

## Task 1: Create a Dictionary of Student Marks

### Program
```python
student_marks = {
    "Alice": 80,
    "John": 79,
    "Mary": 92,
    "David": 85
}

name = input("Enter the student's name: ")
normalized_name = name.strip().lower()

student_marks_lower = {student.lower(): marks for student, marks in student_marks.items()}

if normalized_name in student_marks_lower:
    print(f"{name}'s marks are {student_marks_lower[normalized_name]}")
else:
    print("Student not found")
```

### Sample Input
```text
Enter the student's name: John
```

### Sample Output
```text
John's marks are 79
```

### Sample Input
```text
Enter the student's name: Sarah
```

### Sample Output
```text
Student not found
```

## Task 2: Demonstrate List Slicing

### Program
```python
numbers = list(range(1, 11))
first_five = numbers[:5]
reversed_first_five = first_five[::-1]

print("Extracted list:", first_five)
print("Reversed list:", reversed_first_five)
```

### Sample Output
```text
Extracted list: [1, 2, 3, 4, 5]
Reversed list: [5, 4, 3, 2, 1]
```
