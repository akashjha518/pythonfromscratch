from tkinter import *

# Main application window
root = Tk()
root.title("Calculator")
root.geometry("550x720")
root.resizable(False, False)

# Display field where expressions and results are shown
display = Entry(root,width=25, font=("Arial", 20), bd=10, relief=RIDGE, justify=RIGHT)
display.grid(row=0, column=0, columnspan=3, padx=5, pady=15)


# Append the clicked button value to the display
def click(value):
    display.insert(END, value)


# Remove everything currently shown in the display
def clear():
    display.delete(0, END)


# Evaluate the current expression and replace it with the result
def calculate():
    try:
        expression = display.get()
        result = eval(expression)
        display.delete(0, END)
        display.insert(END, result)
    except:
        display.delete(0, END)
        display.insert(END, "Error")


# Button labels and their grid positions
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2),
    ('0', 4, 0), ('+', 4, 1), ('-', 4, 2),
    ('*', 5, 0), ('/', 5, 1), ('=', 5, 2)
]

# Build the keypad dynamically from the layout above
for (text, row, col) in buttons:
    if text == "=":
        Button(
            root,
            text=text,
            width=12,
            height=2,
            font=("Arial", 12),
            command=calculate
        ).grid(row=row, column=col, padx=5, pady=5)
    else:
        # Capture the current label so each button inserts its own value
        Button(
            root,
            text=text,
            width=12,
            height=2,
            font=("Arial", 12),
            command=lambda t=text: click(t)
        ).grid(row=row, column=col, padx=5, pady=5)

# Clear the full display in one action
Button(
    root,
    text="Clear",
    width=42,
    height=2,
    font=("Arial", 12),
    command=clear
).grid(row=6, column=0, columnspan=3, padx=5, pady=5)

root.mainloop()
