import tkinter as tk

# Function to handle button clicks
def button_click(symbol):
    current_text = entry_var.get()
    entry_var.set(current_text + symbol)

# Function to clear the entry field
def clear():
    entry_var.set("")

# Function to evaluate and display the result
def calculate():
    try:
        result = eval(entry_var.get())
        entry_var.set(str(result))
    except Exception as e:
        entry_var.set("Error")

# Function to validate input (allow only integers)
def validate_input(new_text):
    if not new_text:
        return True
    try:
        int(new_text)
        return True
    except ValueError:
        return False

# Function to handle keyboard number pad input
def num_pad(event):
    key = event.keysym
    if key.isdigit() or key == ".":
        current_text = entry_var.get()
        if current_text and current_text[-1].isdigit():
            return
        button_click(key)
    elif key in ["+", "-", "*", "/"]:
        button_click(key)
    elif key == "Return":
        calculate()
    elif key == "BackSpace":
        entry_var.set(entry_var.get()[:-1])
    elif key == "KP_Add":
        button_click("+")
    elif key == "KP_Subtract":
        button_click("-")
    elif key == "KP_Multiply":
        button_click("*")
    elif key == "KP_Divide":
        button_click("/")

# Create the Tkinter root window
root = tk.Tk()
root.title("Simple Calculator")

# Define and configure the entry widget
entry_var = tk.StringVar()
validate_cmd = root.register(validate_input)
entry = tk.Entry(root, textvariable=entry_var, justify="right", font=("Arial", 20), validate="key", validatecommand=(validate_cmd, "%P"))
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)
entry.focus()

# Define the buttons for the number matrix
buttons = [
    "7", "8", "9",
    "4", "5", "6",
    "1", "2", "3",
]

# Create number buttons and grid them
for i, button in enumerate(buttons):
    row = i // 3 + 1
    col = i % 3
    btn = tk.Button(root, text=button, font=("Arial", 16), padx=20, pady=20, command=lambda b=button: button_click(b))
    btn.grid(row=row, column=col, padx=2, pady=2)  # Adjust padding here

# Create and grid the Clear button
clear_btn = tk.Button(root, text="Clear", font=("Arial", 16), padx=20, pady=20, command=clear,  bg="lightcoral")
clear_btn.grid(row=4, column=0, columnspan=1, padx=5, pady=5)

# Create and grid the "=" button near the Clear button
equal_btn = tk.Button(root, text="=", font=("Arial", 16), padx=20, pady=20, command=calculate, bg="lightblue")
equal_btn.grid(row=4, column=1, columnspan=1, padx=5, pady=5)

# Create and grid the "0" button
zero_btn = tk.Button(root, text="0", font=("Arial", 16), padx=20, pady=20, command=lambda: button_click("0"))
zero_btn.grid(row=4, column=2, padx=2, pady=2)

# Create and grid the "=" button
equal_btn = tk.Button(root, text="=", font=("Arial", 16), padx=20, pady=20, command=calculate)
equal_btn.grid(row=4, column=3, padx=5, pady=5)

# Define the arithmetic operations
operations = ["+", "-", "*", "/"]

# Create and grid the operation buttons
for i, op in enumerate(operations):
    btn = tk.Button(root, text=op, font=("Arial", 16), padx=20, pady=20, command=lambda o=op: button_click(o),bg="light green")
    btn.grid(row=i+1, column=3, padx=5, pady=5)  # Adjust padding here

# Bind the keyboard events to the num_pad function
root.bind("<Key>", num_pad)

# Start the Tkinter event loop
root.mainloop()
