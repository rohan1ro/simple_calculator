import tkinter as tk

def button_click(value):
    """Handles button click events to update the entry field."""
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + value)

def clear():
    """Clears the entry field."""
    entry.delete(0, tk.END)

def calculate():
    """Evaluates the expression in the entry field."""
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# Create the main window
root = tk.Tk()
root.title("Calculator")
root.configure(bg="blue")  # Set background color to blue

# Entry field for displaying the calculation
entry = tk.Entry(root, width=30, borderwidth=5, font=('Arial', 14), justify='right')
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="nsew")

# Button layout
buttons = [
    ('1', 1, 0), ('2', 1, 1), ('3', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('7', 3, 0), ('8', 3, 1), ('9', 3, 2), ('-', 3, 3),
    ('C', 4, 0), ('0', 4, 1), ('=', 4, 2), ('+', 4, 3),
]

# Create buttons and place them in the grid
for text, row, col in buttons:
    if text == 'C':
        button = tk.Button(root, text=text, font=('Arial', 12), bg="lightgray", command=clear)
    elif text == '=':
        button = tk.Button(root, text=text, font=('Arial', 12), bg="lightgray", command=calculate)
    else:
        button = tk.Button(root, text=text, font=('Arial', 12), bg="lightgray", command=lambda t=text: button_click(t))
    button.grid(row=row, column=col, sticky="nsew", padx=5, pady=5)

# Configure grid weights for responsiveness
for i in range(5):  # 5 rows
    root.grid_rowconfigure(i, weight=1)
for j in range(4):  # 4 columns
    root.grid_columnconfigure(j, weight=1)

# Run the application
root.mainloop()
