# Task 1: Dictionary of student marks
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
